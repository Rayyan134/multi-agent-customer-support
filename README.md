# LLM-Powered Multi-Agent Customer Support System

A production-style AI system that demonstrates **LLM-based agent orchestration** using FastAPI and a modular multi-agent architecture.

Instead of relying on static rules or keyword matching, this system uses an **LLM router** to dynamically decide which specialized agent should handle each user request.

---

## Key Idea

Traditional systems use fixed logic like:

"if message contains 'shipping' → go to shipping agent"

This project replaces that with:

An LLM-powered routing layer that understands user intent and selects the correct agent dynamically.

---

## System Architecture
```
User 
  ↓ 
FastAPI Server (/chat) 
  ↓ 
LLM Router (Intelligent Decision Layer)
  ├── Product Agent
  └── Shipping Agent
```
---

## How It Works

1. User sends a message via `/chat`
2. The request is passed to the **LLM Router**
3. The LLM analyzes intent and decides:
   - `product` → product-related queries
   - `shipping` → delivery & logistics queries
4. The selected agent processes the request
5. A structured response is returned to the user

---

## Features

- LLM-based intelligent routing (no hardcoded rules)
- Product information agent (price, stock, details)
- Shipping & delivery agent (timelines, logistics)
- FastAPI REST API backend
- Docker containerization
- Secure environment variable handling
- Modular multi-agent architecture

---

## Why This Project Matters

This project demonstrates how modern AI systems are built:

Instead of a single large model doing everything, real-world systems use:

- Specialized agents
- An orchestration layer
- LLM-based decision-making

This reflects the direction of production AI systems in industry today.

---

## 📡 API Usage

### Endpoint
`POST /chat`

### Request
```json
{
  "message": "Is the iPhone 15 Pro in stock?"
}
```
### Response
```json
{
  "response": "iPhone 15 Pro costs $999 and is currently in stock."
}
```
---
## Key Concepts Demonstrated
* LLM-based routing (intelligent decision layer)
* Multi-agent system design
* Agent orchestration patterns
* Separation of concerns in AI systems
* API development with FastAPI
* Secure configuration using environment variables
* Containerized deployment with Docker

## Future Improvements
* Add confidence scores from LLM router
* Add more specialist agents (returns, warranty, orders)
* Add logging & tracing for agent decisions
* Add evaluation metrics for routing accuracy
* Deploy to cloud (AWS / GCP / Render)

## Tech Stack
* Python 3.11
* FastAPI
* OpenAI API
* Docker
* Uvicorn

## Project Goal

To simulate how production AI systems move from:

simple rule-based logic → LLM-driven intelligent orchestration systems

---
## How to Run the Project
### 1. Clone the repository
```
git clone https://github.com/YOUR_USERNAME/multi-agent-customer-support.git
cd multi-agent-customer-support
```
### 2. Set up environment variables

Create a .env file in the root directory:
```
OPENAI_API_KEY=your_api_key_here
```
#### Important:

Never share or commit this file
It is ignored via .gitignore

### 3. Install dependencies (Local Run)
```
pip install -r requirements.txt
```

### 4. Run the FastAPI server
```
uvicorn main:app --reload
```
Then open in your browser:
```
http://127.0.0.1:8000/docs
```
You can test the API directly using Swagger UI.

### Run with Docker (Recommended)
#### 1. Build the Docker image
```
docker build -t multi-agent-system .
```
#### 2. Run the container
```
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_api_key_here \
  multi-agent-system
```

### 3. Access the API
```
http://127.0.0.1:8000/docs
```

#### Example Test Request
POST /chat
```json
{
  "message": "Is the iPhone 15 Pro in stock?"
}
```
Response
```json
{
  "response": "iPhone 15 Pro costs $999 and is currently in stock."
}
```
