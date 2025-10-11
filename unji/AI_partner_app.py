import streamlit as st
import os
import streamlit_authenticator as stauth 
import yaml
from yaml.loader import SafeLoader
import psycopg2 
from datetime import date # 날짜 처리를 위해 추가

# --- 1. Supabase DB 연결 함수 ---
# @st.cache_resource를 사용하여 앱이 재실행되어도 DB 연결을 유지하고 리소스를 절약합니다.
@st.cache_resource
def get_db_connection():
    """Streamlit secrets를 사용하여 Supabase에 연결합니다."""
    try:
        # secrets.toml에 있는 db_connection_string을 사용합니다.
        conn = psycopg2.connect(st.secrets["db_connection_string"])
        return conn
    except Exception as e:
        # DB 연결 오류 시 사용자에게 메시지를 표시합니다.
        st.error(f"데이터베이스 연결 오류가 발생했습니다. '.streamlit/secrets.toml' 파일을 확인해주세요: {e}")
        return None

def load_user_schedules(conn, user_id):
    """특정 사용자의 일정 데이터를 DB에서 가져옵니다."""
    if not conn: return []
    try:
        with conn.cursor() as cur:
            # 해당 user_id를 가진 일정만 조회합니다.
            cur.execute(
                "SELECT title, schedule_date FROM schedules WHERE user_id = %s ORDER BY schedule_date DESC", 
                (user_id,)
            )
            data = cur.fetchall()
            # 데이터를 Streamlit이 보기 좋은 형식으로 변환합니다.
            return [{"제목": row[0], "날짜": row[1].strftime('%Y-%m-%d')} for row in data]
    except Exception as e:
        st.error(f"일정 로드 오류: {e}")
        return []

def save_user_schedule(conn, user_id, title, schedule_date):
    """새 일정을 DB에 저장합니다."""
    if not conn: return False
    try:
        with conn.cursor() as cur:
            # INSERT 쿼리를 실행하여 새 일정을 저장합니다.
            cur.execute(
                "INSERT INTO schedules (user_id, title, schedule_date) VALUES (%s, %s, %s)",
                (user_id, title, schedule_date)
            )
            conn.commit() # 변경 사항을 최종적으로 DB에 반영합니다.
        return True
    except Exception as e:
        st.error(f"일정 저장 오류: {e}")
        conn.rollback() # 오류 시 커밋을 취소합니다.
        return False

# --- 2. 초기 설정 및 DB 연결 시도 ---
st.set_page_config(layout="wide")
st.title("AI Plan Partner")

# DB 연결을 시도하고 연결 객체를 얻습니다.
conn = get_db_connection()


# --- 3. 사용자 인증 설정 및 로그인 처리 ---
try:
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
except FileNotFoundError:
    st.error("config.yaml 파일을 찾을 수 없습니다. 1단계 파일을 확인해주세요.")
    st.stop()
except Exception as e:
    st.error(f"config.yaml 파일 로드 오류: {e}")
    st.stop()


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# 로그인 UI 표시 및 결과 확인
name, authentication_status, username = authenticator.login('로그인', 'main')


if authentication_status:
    # =================================================================
    # === 로그인 성공 시: 메인 앱 UI 및 개인화 기능 표시 ===
    # =================================================================
    st.session_state['user_id'] = username
    
    # 사이드바에 로그아웃 버튼과 환영 메시지 표시
    with st.sidebar:
        authenticator.logout('로그아웃', 'main')
        st.markdown(f"**환영합니다, {name}님!**")

        # --- A. 파일 업로드 기능 (사이드바) ---
        st.subheader("파일 업로드")
        uploaded_file = st.file_uploader("새 파일 업로드", type=['pdf', 'txt', 'docx'])

        if uploaded_file is not None:
            # 🚨 실제 서버에서는 이 파일을 Supabase Storage 또는 S3 등에 user_id와 함께 저장해야 합니다.
            # 현재는 파일이 업로드되었다는 메시지만 표시합니다.
            st.success(f"'{uploaded_file.name}' 업로드 완료! (서버 저장 로직 필요)")
            # save_file_to_storage(username, uploaded_file) # 실제 저장 함수 호출

    
    # --- B. 일정 생성 폼 (메인 영역) ---
    st.subheader("나의 일정 생성")
    
    # st.form을 사용하여 폼 제출 시에만 서버 호출이 일어나도록 효율적으로 만듭니다.
    with st.form("schedule_form", clear_on_submit=True):
        col1, col2, col3 = st.columns([3, 2, 1])
        with col1:
            schedule_title = st.text_input("일정 제목", max_chars=100)
        with col2:
            schedule_date = st.date_input("날짜", value=date.today())
        with col3:
            st.markdown("<br>", unsafe_allow_html=True) # 공간 확보
            submitted = st.form_submit_button("일정 저장")

    if submitted:
        if conn and schedule_title:
            # DB 저장 함수 호출
            if save_user_schedule(conn, username, schedule_title, schedule_date):
                st.success(f"새 일정 **'{schedule_title}'**이 저장되었습니다.")
            # 실패 메시지는 save_user_schedule 함수 내에서 처리됨
        else:
            st.warning("일정 제목을 입력해주세요.")


    # --- C. 사용자별 일정 목록 표시 ---
    st.subheader(f"📅 {name}님의 일정 목록")
    
    # load_user_schedules 함수를 호출하여 DB에서 현재 사용자의 일정만 가져옵니다.
    user_schedules = load_user_schedules(conn, username)
    
    if user_schedules:
        # 데이터프레임으로 깔끔하게 표시
        st.dataframe(user_schedules, use_container_width=True, hide_index=True)
    else:
        st.info("저장된 일정이 없습니다. 새 일정을 추가해보세요!")

    
    # --- D. 기존 HTML UI 렌더링 (옵션) ---
    # 기존 HTML 파일은 일정 관리 로직이 제거된 순수 UI 구성 요소만 남아있다고 가정합니다.
    # html_file_path = "unji/htmls/AI_partner.html"
    # try:
    #     with open(html_file_path, "r", encoding="utf-8") as f:
    #         html_content = f.read()
    #     st.components.v1.html(html_content, height=500, scrolling=True)
    # except FileNotFoundError:
    #     # HTML 파일 경로를 현재 프로젝트 구조에 맞게 수정해주세요.
    #     pass


elif authentication_status is False:
    st.error('사용자 이름 또는 비밀번호가 올바르지 않습니다.')
    st.info('테스트 계정: ID=testuser, PW=123')
elif authentication_status is None:
    st.info('로그인이 필요합니다. 왼쪽 상단에서 로그인해주세요.')
