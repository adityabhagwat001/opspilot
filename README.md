# OpsPilot 🚀
> **Enterprise Operations AI Agent with Model Context Protocol (MCP) & Human-in-the-Loop (HITL) Security Engine**

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Next.js 14](https://img.shields.io/badge/Next.js-14.0+-000000?style=flat&logo=next.js&logoColor=white)](https://nextjs.org)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=flat&logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Executive Summary & Problem Statement

Enterprise Operations teams (DevOps, IT, Support, Systems Engineers) frequently switch contexts across fragmented tool interfaces: querying databases, inspecting GitHub repositories, running shell commands, and sending notification emails.

Existing generic AI assistants pose serious operational risks: plain LLM tool integrations can execute destructive commands (`DROP TABLE`, `git push --force`, unverified email broadcasts) directly against production environments without guardrails.

**OpsPilot** solves this by combining **Model Context Protocol (MCP)** tool integration with a deterministic **Human-in-the-Loop (HITL) Security Engine**. Any state-changing mutation (`INSERT`, `UPDATE`, `DELETE`, `git push`, sending external messages) automatically triggers a state machine breakpoint, suspending agent execution and requiring explicit human administrator review before proceeding.

---

## 🏗️ High-Level System Architecture

```
[ User Browser / Next.js UI ] ◄──(WebSockets / SSE)──► [ FastAPI Backend ]
                                                            │
                                                            ▼
                                                [ LangGraph Agent Executor ]
                                                            │
                                                            ▼
                                               [ HITL Approval State Machine ]
                                                            │
                                          ┌─────────────────┴─────────────────┐
                                          │ (Mutation Tool Call Detoured)     │ (Read Tool Allowed)
                                          ▼                                   ▼
                              [ Pending Approval Ticket ]         [ MCP Client Orchestration ]
                                          │                                   │
                                 (Admin Approves via UI)                      │
                                          │                                   │
                                          └─────────────────┬─────────────────┘
                                                            │
                                                            ▼
                                             [ Python MCP Server Infrastructure ]
                                              ├── PostgreSQL MCP Server
                                              ├── GitHub MCP Server
                                              └── Communication MCP Server
```

---

## 🛠️ Technology Stack

- **Backend Framework:** FastAPI (Python 3.11+ async)
- **Agent Orchestration:** LangGraph + MCP Python SDK
- **Frontend Framework:** Next.js 14 (App Router, TypeScript, Tailwind CSS, Shadcn UI)
- **Primary Database:** PostgreSQL 16 (Relational DB, Audit Logs, State Machines)
- **In-Memory Cache & Pub/Sub:** Redis 7 (WebSocket session events, rate limiting, cache)
- **Containerization & Deployment:** Docker & Docker Compose
- **Testing Framework:** Pytest, Playwright, GitHub Actions CI/CD

---


## 🚀 Quickstart & Local Setup

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Node.js 18+ (for frontend)

### Environment Setup
```bash
# Clone the repository
git clone https://github.com/<your-username>/opspilot.git
cd opspilot

# Copy environment template
cp .env.example .env
```

### Running with Docker Compose
```bash
docker compose up --build -d
```

Access the API documentation at: `http://localhost:8000/docs`

---

## 🧪 Testing

Run backend test suite using Pytest:
```bash
cd backend
pytest tests/ -v
```

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
