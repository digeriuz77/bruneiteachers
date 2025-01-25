import streamlit as st
from tasks import (
    prompt_improver,
    mcq_maker,
    hinge_question_maker,
    lesson_objectives,
    adaptive_practice,
)

# Streamlit App Title
st.title("📚 AI Lesson Assistant")
st.caption("🚀 Powered by Google Gemini")

# Initialize session state for API key
if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = None

# Sidebar for API Key Configuration and Task Buttons
with st.sidebar:
    st.header("API Configuration")
    gemini_api_key = st.text_input("Google Gemini API Key", type="password")
    if st.button("Save API Key"):
        st.session_state.gemini_api_key = gemini_api_key
        st.success("API Key Saved!")
    "[Get a Google Gemini API key](https://ai.google.dev/)"

    st.header("Tasks")
    task = st.radio(
        "Select a Task",
        [
            "Prompt Improver",
            "MCQ Maker",
            "Hinge Question Maker",
            "Student-Friendly Lesson Objectives",
            "Adaptive Practice",
        ],
    )

# Task Routing
if task == "Prompt Improver":
    prompt_improver.render(st.session_state.gemini_api_key)
elif task == "MCQ Maker":
    mcq_maker.render(st.session_state.gemini_api_key)
elif task == "Hinge Question Maker":
    hinge_question_maker.render(st.session_state.gemini_api_key)
elif task == "Student-Friendly Lesson Objectives":
    lesson_objectives.render(st.session_state.gemini_api_key)
elif task == "Adaptive Practice":
    adaptive_practice.render(st.session_state.gemini_api_key)
