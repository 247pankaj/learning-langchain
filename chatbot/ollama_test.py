import os
import streamlit as st
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Load environment variables from .env file
load_dotenv()

# Set LangChain environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to user queries."),
    ("user", "Question: {question}")
])

# Initialize the Ollama LLaMA2 model
llm = Ollama(model="gemma3:4b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Streamlit UI
st.title("LangChain Demo with LLaMA2 via Ollama")
user_input = st.text_input("Enter your question:")

if user_input:
    response = chain.invoke({"question": user_input})
    st.write(response)
