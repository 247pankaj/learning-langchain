import requests
import streamlit as st

# Streamlit UI
st.title("LangChain Demo with OpenAI and LLaMA2")

# Input fields
essay_topic = st.text_input("Write an essay on:")
poem_topic = st.text_input("Write a poem on:")

# API call to OpenAI essay route
def get_openai_response(topic: str) -> str:
    try:
        response = requests.post(
            "http://localhost:8000/essay",
            json={"topic": topic}  # match FastAPI TopicRequest model
        )
        response.raise_for_status()
        return response.json().get("result", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# API call to Ollama poem route
def get_ollama_response(topic: str) -> str:
    try:
        response = requests.post(
            "http://localhost:8000/poem",
            json={"topic": topic}  # match FastAPI TopicRequest model
        )
        response.raise_for_status()
        return response.json().get("result", "No response received.")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Display results
if essay_topic:
    st.subheader("Essay Output")
    st.write(get_openai_response(essay_topic))

if poem_topic:
    st.subheader("Poem Output")
    st.write(get_ollama_response(poem_topic))
