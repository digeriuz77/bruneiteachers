import streamlit as st
from api import call_gemini

def render(api_key):
    st.header("📝 Adaptive Practice")
    lesson_objective = st.text_input("Enter Lesson Objective:")
    if st.button("Generate Adaptive Practice"):
        if not api_key:
            st.error("Please add your Google Gemini API key to continue.")
            return

        prompt = f"""
        Provide adaptive practice suggestions based on the lesson objective: {lesson_objective}
        - Include differentiated activities
        - Suggest resources for varying skill levels
        """
        adaptive_practice = call_gemini(prompt, api_key)
        st.write("Adaptive Practice Suggestions:")
        st.write(adaptive_practice)
