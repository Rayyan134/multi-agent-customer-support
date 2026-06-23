# Multi-Agent Customer Support System (A2A-Inspired)

A modular AI agent system that simulates real-world customer support using **multi-agent orchestration principles** inspired by the Agent-to-Agent (A2A) architecture.

---

## Overview

This project demonstrates how AI agents can be structured as **specialized components** working together through a central orchestrator.

Instead of using one monolithic model, the system routes user queries to dedicated agents:

- Product Catalog Agent → handles product & pricing queries  
- Shipping Agent → handles delivery & logistics queries  
- Customer Support Agent → orchestrates routing between agents  

---

## Architecture

User
↓
FastAPI Server (/chat)
↓
CustomerSupportAgent (Orchestrator)
├── ProductCatalogAgent
└── ShippingAgent


---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- Docker

---

## API Endpoint

### POST `/chat`

Request:
```json
{
  "message": "Is the iPhone 15 Pro in stock?"
}

Response:

{
  "response": "iPhone 15 Pro costs $999 and is currently in stock."
}