# TASK 6 – System Design & Deployment Concepts 

## Goal
This document explains core system design and deployment concepts used in real-world backend and AI systems.  
For each concept, it answers:
- Where it should be used  
- Where it should be avoided  
- What can break if it is misused  
A simple architecture diagram is also included.

---

## 1. Monolith vs Microservices

### Monolith Architecture

**Where to use**
- Small to medium-sized applications
- Early-stage startups
- Projects with small teams
- When fast development is more important than scalability

**Where to avoid**
- Very large systems with many independent features
- Applications requiring independent scaling of components

**What breaks if misused**
- Codebase becomes tightly coupled
- Small changes can affect the entire system
- Scaling becomes difficult as the application grows

---

### Microservices Architecture

**Where to use**
- Large-scale systems
- Applications with multiple independent modules
- Teams working on different services simultaneously
- Systems requiring high scalability and fault isolation

**Where to avoid**
- Small projects
- Teams without DevOps or deployment experience

**What breaks if misused**
- Increased complexity
- Network failures between services
- Difficult debugging and monitoring
- Higher infrastructure cost

---

## 2. Sync vs Async APIs

### Synchronous APIs

**Where to use**
- Simple CRUD applications
- Operations that complete quickly
- When immediate response is required

**Where to avoid**
- Long-running tasks
- High-concurrency systems

**What breaks if misused**
- Request blocking
- Poor performance under load
- Reduced scalability

---

### Asynchronous APIs

**Where to use**
- AI processing
- File uploads
- External API calls
- High-concurrency systems

**Where to avoid**
- Very simple applications
- Teams unfamiliar with async programming

**What breaks if misused**
- Hard-to-debug code
- Improper async usage can still block execution
- Resource leaks if tasks are not handled correctly

---

## 3. FastAPI with Uvicorn

### FastAPI

**Where to use**
- REST API development
- AI and ML backends
- Applications requiring high performance
- APIs needing automatic documentation

**Where to avoid**
- Extremely simple scripts where a framework is unnecessary

**What breaks if misused**
- Poor performance if blocking code is used
- Incorrect async usage reduces benefits

---

### Uvicorn

**Where to use**
- Running FastAPI applications
- ASGI-based applications
- High-performance API servers

**Where to avoid**
- Running production systems without process managers (e.g., Gunicorn workers)

**What breaks if misused**
- Server crashes under heavy load
- Poor fault tolerance in production

---

## 4. Docker (Conceptual)

**Where to use**
- Application deployment
- Environment consistency
- CI/CD pipelines
- Cloud deployments

**Where to avoid**
- Very small local-only scripts
- Systems with strict hardware constraints

**What breaks if misused**
- Large image sizes
- Slow builds
- Security vulnerabilities if images are not maintained

---

## 5. API Security

### API Keys

**Where to use**
- Authenticating external clients
- Protecting paid or private APIs

**Where to avoid**
- Public, open-access APIs

**What breaks if misused**
- Key leakage leads to unauthorized access
- Financial loss due to abuse

---

### Rate Limiting

**Where to use**
- Public APIs
- AI services
- Preventing abuse and DDoS attacks

**Where to avoid**
- Internal trusted services (unless required)

**What breaks if misused**
- Legitimate users may get blocked
- Poor user experience if limits are too strict

---

## Simple Architecture Diagram
Client
|
v
API Gateway / FastAPI
|
v
Async Processing Layer
|
v
AI Logic / Business Rules
|
v
Database / Storage

## Summary

- Monoliths are simpler but harder to scale.
- Microservices scale well but add complexity.
- Sync APIs are easy but block execution.
- Async APIs improve performance for long tasks.
- FastAPI with Uvicorn offers high performance.
- Docker ensures consistent deployment.
- API security is essential to protect systems.


