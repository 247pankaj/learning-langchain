import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key (expects it in .env as OPENAI_API_KEY)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server exposing LangChain routes",
)

# Base models
openai_model = ChatOpenAI()
ollama_model = OllamaLLM(model="gemma3:4b")

# Prompt templates
essay_prompt = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words."
)

poem_prompt = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5-year-old child, limited to 100 words."
)

# Add LangServe routes
add_routes(app, openai_model, path="/openai")
add_routes(app, essay_prompt | openai_model, path="/essay")
add_routes(app, poem_prompt | ollama_model, path="/poem")

# Run the server
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
