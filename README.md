# AutoStream AI Agent

A conversational AI agent built for the Machine Learning Intern assignment.

This project simulates a real-world **social-to-lead workflow** for a fictional SaaS company called **AutoStream**, which provides automated video editing tools for content creators.

The agent can:
- identify user intent
- answer pricing and policy questions from a local knowledge base
- detect high-intent users
- collect lead details
- trigger a mock lead capture function

---

## Features

- **Intent Detection**
  - Greeting
  - Pricing or product inquiry
  - High-intent lead

- **Knowledge Retrieval (RAG-style)**
  - Uses a local JSON knowledge base
  - Answers questions about plans, features, refunds, and support

- **Lead Capture Workflow**
  - Collects:
    - Name
    - Email
    - Creator platform
  - Executes tool logic only after all required details are collected

- **State Management**
  - Maintains conversation state across multiple turns

---

## Project Structure

```text
autostream-ai-agent/
│── main.py
│── knowledge_base.json
│── requirements.txt
│── README.md
│── .gitignore
