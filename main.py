from fastapi import FastAPI
from pydantic import BaseModel

from agents.customer_support import CustomerSupportAgent

app = FastAPI(
    title="Multi-Agent Customer Support API",
    description="A simple multi-agent system inspired by A2A concepts.",
    version="1.0.0",
)

agent = CustomerSupportAgent()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {
        "message": "Welcome to the Multi-Agent Customer Support API!",
        "docs": "/docs",
    }


@app.post("/chat")
def chat(request: ChatRequest):
    response = agent.handle_query(request.message)
    return {"response": response}