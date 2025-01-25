import streamlit as st
from api import call_gemini

def render(api_key):
    st.header("📝 Prompt Improver")
    teacher_prompt = st.text_area("Enter your prompt:")
    if st.button("Improve Prompt"):
        if not api_key:
            st.error("Please add your Google Gemini API key to continue.")
            return

        improved_prompt = f"""
        <goal>{teacher_prompt}</goal>
        <context>Provide specific context here</context>
        <format>Define the desired output format</format>
        """
        st.write("Improved Prompt:")
        st.code(improved_prompt)
