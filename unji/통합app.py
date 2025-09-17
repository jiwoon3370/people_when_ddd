import streamlit as st
import os

# Streamlit 앱 설정
st.set_page_config(layout="wide")
st.title("정보과제연구 실습 모음")

# HTML 파일 경로 매핑
html_files = {
    "메인 페이지": "unji/htmls/index.html",
    "조추첨": "unji/htmls/조추첨.html",
    "첸토": "unji/htmls/첸토.html"
    "HP스택 시스템": "unji/htmls/stack_hp.html"
}

# 사이드바에서 페이지 선택
selected_page = st.sidebar.selectbox("📄 페이지 선택", list(html_files.keys()))

# 선택된 HTML 파일 경로
html_file_path = html_files[selected_page]

# HTML 파일 로드 및 렌더링
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    st.components.v1.html(html_content, height=1000, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: '{html_file_path}' 파일을 찾을 수 없습니다. 해당 폴더 안에 파일이 있는지 확인해주세요.")
except Exception as e:
    st.error(f"파일을 읽는 도중 오류가 발생했습니다: {e}")
