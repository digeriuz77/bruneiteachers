import streamlit as st
import openai
import google.generativeai as genai
import deepseek

# Initialize session state
if 'api_key' not in st.session_state:
    st.session_state.api_key = None
if 'api_provider' not in st.session_state:
    st.session_state.api_provider = None

# Sidebar for API configuration
with st.sidebar:
    st.title("API Configuration")
    api_provider = st.selectbox("Select API Provider", ["Google Gemini", "OpenAI", "DeepSeek"])
    api_key = st.text_input("Enter API Key", type="password")
    if st.button("Save API Key"):
        st.session_state.api_key = api_key
        st.session_state.api_provider = api_provider
        st.success("API Key Saved!")

# Main App
st.title("AI Lesson Assistant")

# Function to call the appropriate API
def call_api(prompt):
    if st.session_state.api_provider == "Google Gemini":
        genai.configure(api_key=st.session_state.api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        return response.text
    elif st.session_state.api_provider == "OpenAI":
        openai.api_key = st.session_state.api_key
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text
    elif st.session_state.api_provider == "DeepSeek":
        # Assuming DeepSeek has a similar API structure
        deepseek.api_key = st.session_state.api_key
        response = deepseek.Completion.create(
            model="deepseek-model",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text
    else:
        st.error("Please configure the API key and provider.")
        return None

# Prompt Improver
st.header("Prompt Improver")
teacher_prompt = st.text_area("Enter your prompt:")
if st.button("Improve Prompt"):
    improved_prompt = f"""
    <goal>{teacher_prompt}</goal>
    <context>Provide specific context here</context>
    <format>Define the desired output format</format>
    """
    st.write("Improved Prompt:")
    st.code(improved_prompt)

# MCQ Maker
st.header("MCQ Maker")
lesson_objective = st.text_input("Enter Lesson Objective:")
key_concepts = st.text_input("Enter Key Concepts:")
if st.button("Generate MCQs"):
    prompt = f"Create 5 MCQs for: {lesson_objective}\nKey concepts: {key_concepts}\n- 4 options per question\n- Highlight common misconceptions\n- Avoid trick questions"
    mcqs = call_api(prompt)
    st.write("Generated MCQs:")
    st.write(mcqs)

# Hinge Question Maker
st.header("Hinge Question Maker")
if st.button("Generate Hinge Questions"):
    prompt = "Generate hinge questions based on the lesson objective and key concepts."
    hinge_questions = call_api(prompt)
    st.write("Generated Hinge Questions:")
    st.write(hinge_questions)

# Student-Friendly Lesson Objectives
st.header("Student-Friendly Lesson Objectives")
if st.button("Generate Lesson Objectives"):
    prompt = "Generate student-friendly lesson objectives and steps to success."
    lesson_objectives = call_api(prompt)
    st.write("Generated Lesson Objectives:")
    st.write(lesson_objectives)

# Adaptive Practice
st.header("Adaptive Practice")
if st.button("Generate Adaptive Practice"):
    prompt = "Provide adaptive practice suggestions based on the structured data table."
    adaptive_practice = call_api(prompt)
    st.write("Adaptive Practice Suggestions:")
    st.write(adaptive_practice)
