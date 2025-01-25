import streamlit as st
from api import call_gemini

def render(api_key):
    st.header("📝 Student-Friendly Lesson Objectives")
    lesson_objective = st.text_input("Enter Lesson Objective:")
    if st.button("Generate Lesson Objectives"):
        if not api_key:
            st.error("Please add your Google Gemini API key to continue.")
            return

        prompt = f"""
        Generate student-friendly lesson objectives and steps to success for: {lesson_objective}
        - Use simple language
        - Break down into clear steps
        """
        objectives = call_gemini(prompt, api_key)
        st.write("Generated Lesson Objectives:")
        st.write(objectives)
