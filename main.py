import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("AI API 실습")

# 대화 내용 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
# 이전 대화 출력
for role, text in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(text)
#사용자 입력 및 처리
if question := st.chat_input("질문을 입력하세요."):
    with st.chat_message("user"):
        st.write(question)
    st.session_state.chat_history.append(("user", question))

    chat = client.chats.create(model="gemini-2.5-flash")
# API 호출 (response는 if문 안에서만 유효)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            {"role": r if r == "user" else "model", "parts": [{"text": t}]}
            for r, t in st.session_state.chat_history
        ],
    )
# AI 응답 표시 및 저장
    with st.chat_message("assistant"):
        st.write(response.text)
    st.session_state.chat_history.append(("assistant", response.text))
