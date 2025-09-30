import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()
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

# --- Pydantic request/response models ---
class TopicRequest(BaseModel):
    topic: str

class ResultResponse(BaseModel):
    result: str

# --- Routes with explicit request/response models ---
@app.post("/openai", response_model=ResultResponse)
async def openai_endpoint(req: TopicRequest):
    output = openai_model.invoke({"input": req.topic})
    return ResultResponse(result=output)

@app.post("/essay", response_model=ResultResponse)
async def essay_endpoint(req: TopicRequest):
    chain = essay_prompt | openai_model
    output = chain.invoke({"topic": req.topic})
    return ResultResponse(result=output)

@app.post("/poem", response_model=ResultResponse)
async def poem_endpoint(req: TopicRequest):
    chain = poem_prompt | ollama_model
    output = chain.invoke({"topic": req.topic})
    return ResultResponse(result=output)

# Run the server
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
