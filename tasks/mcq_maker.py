import streamlit as st
from api import call_gemini

def render(api_key):
    st.header("📝 MCQ Maker")
    lesson_objective = st.text_input("Enter Lesson Objective:")
    key_concepts = st.text_input("Enter Key Concepts:")
    if st.button("Generate MCQs"):
        if not api_key:
            st.error("Please add your Google Gemini API key to continue.")
            return

        prompt = f"""
        Create 5 MCQs for: {lesson_objective}
        Key concepts: {key_concepts}
        - 4 options per question
        - Highlight common misconceptions
        - Avoid trick questions
        """
        mcqs = call_gemini(prompt, api_key)
        st.write("Generated MCQs:")
        st.write(mcqs)
