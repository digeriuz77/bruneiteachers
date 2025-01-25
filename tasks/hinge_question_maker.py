import streamlit as st
from api import call_gemini

def render(api_key):
    st.header("📝 Hinge Question Maker")
    lesson_objective = st.text_input("Enter Lesson Objective:")
    if st.button("Generate Hinge Questions"):
        if not api_key:
            st.error("Please add your Google Gemini API key to continue.")
            return

        prompt = f"""
        Generate hinge questions based on the lesson objective: {lesson_objective}
        - Ensure questions check for understanding of key concepts
        - Provide clear and concise questions
        """
        hinge_questions = call_gemini(prompt, api_key)
        st.write("Generated Hinge Questions:")
        st.write(hinge_questions)
