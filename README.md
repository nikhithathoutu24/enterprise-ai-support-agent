# Enterprise Agentic AI Support Platform

An enterprise-grade AI support platform that combines local Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), vector search, customer context retrieval, and Jira automation to intelligently process support requests.

## Overview

This project simulates a real-world enterprise support workflow where customer requests are analyzed by an AI agent, enriched with contextual knowledge, and automatically routed through Jira for issue tracking.

The platform leverages a local LLM using Ollama and Llama 3.2, ChromaDB for semantic search, and FastAPI and Streamlit for backend and frontend services.

---

## Features

### AI-Powered Ticket Classification

* Intent detection using Llama 3.2
* Priority assignment
* AI-generated issue summaries

### Retrieval-Augmented Generation (RAG)

* ChromaDB vector database
* Semantic similarity search
* Knowledge base retrieval
* Context-aware support recommendations

### Customer Context Retrieval

* Customer profile lookup
* Account status retrieval
* Subscription and company information

### Jira Automation

* Automatic Jira issue creation
* Priority-based ticket routing
* Ticket tracking and monitoring

### Interactive Frontend

* Streamlit-based support portal
* Real-time AI processing
* Knowledge base insights
* Jira ticket visibility

---

## System Architecture

Customer Request

↓

Streamlit Frontend

↓

Agent Orchestrator

↓

Llama 3.2 (Ollama)

↓

Intent Classification

↓

Customer Context Retrieval

↓

ChromaDB Semantic Search

↓

Knowledge Retrieval (RAG)

↓

Jira Ticket Creation

↓

AI Response

---

## Technology Stack

### Artificial Intelligence

* Ollama
* Llama 3.2
* Prompt Engineering
* Agentic Workflows

### Retrieval-Augmented Generation

* ChromaDB
* Vector Embeddings
* Semantic Search
* Knowledge Retrieval

### Backend

* Python
* FastAPI
* REST APIs

### Frontend

* Streamlit

### Enterprise Integrations

* Jira Cloud REST API
* Customer Context Service

### Development Tools

* Git
* GitHub
* VS Code

---

## Demo Scenarios

### Login Issue

Input:

```json
{
  "email": "sarah@example.com",
  "message": "My password reset email never arrives and I cannot access my account"
}
```

Output:

* Intent: login_issue
* Priority: high
* Knowledge Source: login_help.txt
* Jira Ticket: ASA-5

### Billing Issue

Input:

```json
{
  "email": "john@example.com",
  "message": "I was charged twice for my subscription this month"
}
```

Output:

* Intent: billing_issue
* Priority: medium
* Jira Ticket Created

### Critical Production Incident

Input:

```json
{
  "email": "mike@example.com",
  "message": "URGENT: Production dashboard is down for all customers"
}
```

Output:

* Priority: critical
* Immediate Jira Escalation

---

## Project Workflow

1. Customer submits a support request.
2. Llama 3.2 classifies the issue.
3. Customer information is retrieved.
4. ChromaDB performs semantic search.
5. Relevant knowledge base content is retrieved.
6. Jira ticket is automatically created.
7. AI response is generated and displayed.

---

## Skills Demonstrated

* Generative AI
* Agentic AI Systems
* Large Language Models (LLMs)
* Retrieval-Augmented Generation (RAG)
* Vector Databases
* Semantic Search
* Prompt Engineering
* REST API Development
* FastAPI
* Streamlit
* Jira Automation
* Enterprise Software Integration
* Git and GitHub

---

## Future Enhancements

* Slack Integration
* Confluence Knowledge Base Integration
* LangChain Tool Agents
* Multi-Agent Orchestration
* React Frontend
* Authentication and RBAC
* Cloud Deployment (AWS/Azure/GCP)

---

## Author

Nikhitha T
