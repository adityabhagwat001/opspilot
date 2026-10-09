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

## 📅 12-Sprint Roadmap (3-Month Development Schedule)

- [x] **Sprint 1 (Days 1–7):** Project Foundation, FastAPI Architecture, Docker Compose & PostgreSQL Migrations (`v0.1.0-foundation`)
- [ ] **Sprint 2 (Days 8–14):** JWT Authentication, RBAC Engine & Next.js UI Skeleton (`v0.2.0-auth-and-ui`)
- [ ] **Sprint 3 (Days 15–21):** Custom Python MCP Servers (PostgreSQL & GitHub) (`v0.3.0-mcp-servers`)
- [ ] **Sprint 4 (Days 22–28):** **MVP RELEASE:** LangGraph Agent Loop + HITL Approval Modal + SSE Streaming (`v1.0.0-mvp`)
- [ ] **Sprint 5 (Days 29–35):** Real-Time WebSockets Alerts & Immutable Audit Logging Engine (`v1.1.0-realtime-audit`)
- [ ] **Sprint 6 (Days 36–42):** Email/Calendar MCP Server & Granular Tool Policy Matrix (`v1.2.0-communication-mcp`)
- [ ] **Sprint 7 (Days 43–49):** Redis Caching, Rate Limiting & Graceful Failure Recovery Engine (`v1.3.0-resilience-caching`)
- [ ] **Sprint 8 (Days 50–56):** **PRODUCTION CORE:** GitHub Actions CI/CD & Playwright E2E Testing (`v1.4.0-production-core`)
- [ ] **Sprint 9 (Days 57–63):** Dynamic MCP Server Registry UI & Encrypted Secret Vault (`v1.5.0-mcp-registry`)
- [ ] **Sprint 10 (Days 64–70):** Operations Analytics Dashboard & Compliance Export (`v1.6.0-analytics`)
- [ ] **Sprint 11 (Days 71–77):** Load Latency Benchmarks, Security Audit & Interview Defense Prep (`v1.7.0-benchmarks-security`)
- [ ] **Sprint 12 (Days 78–84):** **FINAL RELEASE:** Cloud Deployment, Live Video Demo & Release (`v2.0.0-final-release`)

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
