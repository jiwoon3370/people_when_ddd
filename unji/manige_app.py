import streamlit as st
import os

# Streamlit 앱 설정
st.set_page_config(layout="wide")
st.title("학습 일정/과제 관리 ai")

# HTML 파일의 경로를 지정합니다.
html_file_path = "unji/htmls/manige.html"

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # HTML 콘텐츠를 Streamlit 앱에 렌더링합니다.
    st.components.v1.html(html_content, height=1000, scrolling=True)

except FileNotFoundError:
    st.error(f"오류: '{html_file_path}' 파일을 찾을 수 없습니다. 'htmls' 폴더 안에 'index.html' 파일이 있는지 확인해주세요.")
except Exception as e:
    st.error(f"파일을 읽는 도중 오류가 발생했습니다: {e}")

