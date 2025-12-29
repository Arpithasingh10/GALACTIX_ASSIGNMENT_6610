# Internship Assignment – AI/ML Domain

## Overview

This repository contains my completed internship assignment focused on **Artificial Intelligence, Machine Learning, Data Engineering, Backend Development, and System Design**.  
The assignment was designed to evaluate real-world engineering thinking, not just coding skills.

The work is divided into **six tasks**, each addressing a specific engineering concept such as data preprocessing, API development, asynchronous processing, AI integration, and system design fundamentals.

---

## Technologies Used

- Python  
- FastAPI  
- Pydantic  
- Asyncio  
- SQL / MySQL (conceptual & practical usage)  
- PowerShell (for concurrency testing)  
- Swagger UI  
- GitHub  

---

## Folder Structure

├── Task1_Data_Engineering/
│ ├── data_utils.py
│ ├── sample_data/
│ └── observations.md
│
├── Task2_FastAPI_Backend/
│ ├── main.py
│ └── design_decisions.md
│
├── Task3_Async_vs_Sync/
│ ├── main.py
│ ├── performance_results.csv
│ └── analysis.md
│
├── Task4_AI_API_Integration/
│ ├── ai_results.json
│ └── prompt_analysis.md
│
├── Task5_Mini_AI_System/
│ ├── main.py
│ └── problem_statement.md
│
├── Task6_System_Design/
│ └── README.md
│
└── README.md


---

## Task-Wise Explanation & Approach

---

### TASK 1 – Data Engineering Foundations

**Objective:**  
Understand real-world data issues and design reusable Python utilities.

**Approach:**  
- Created a custom HR Attrition dataset with more than 50 records.
- Dataset intentionally includes:
  - Missing values
  - Duplicate records
  - Mixed data types
  - Outliers
- Implemented reusable functions to:
  - Detect missing values
  - Detect duplicate rows
  - Identify basic outliers
  - Normalize numeric columns
  - Remove duplicates using a custom rule
- Avoided hardcoding column names to ensure reusability.

**Outcome:**  
Developed a strong understanding of data cleaning and preprocessing, which is critical for analytics and machine learning pipelines.

---

### TASK 2 – Backend API Development with FastAPI

**Objective:**  
Build a REST API with clear structure and design decisions.

**Approach:**  
- Built a FastAPI backend with the following endpoints:
  - `POST /data`
  - `GET /data`
  - `GET /health`
- Used Pydantic models for request validation.
- Implemented proper HTTP status codes and error handling.
- Stored data in memory to focus on API behavior rather than database complexity.

**Design Decision:**  
In-memory storage was chosen to keep the system simple and emphasize API design principles.

---

### TASK 3 – Async vs Sync Performance Experiment

**Objective:**  
Understand when asynchronous programming improves performance.

**Approach:**  
- Implemented:
  - A synchronous endpoint using `time.sleep()`
  - An asynchronous endpoint using `asyncio.sleep()`
- Tested:
  - Single request
  - 10 concurrent requests
- Used PowerShell background jobs and Swagger UI tabs to simulate concurrency.
- Measured execution time directly from API responses.

**Outcome:**  
Observed that synchronous endpoints block execution, while asynchronous endpoints efficiently handle concurrent requests.

---

### TASK 4 – AI API Integration & Prompt Experimentation

**Objective:**  
Integrate AI thoughtfully and analyze prompt behavior.

**Approach:**  
- Chose **Sentiment Analysis** as the AI task.
- Designed three different prompts for the same input text.
- Implemented API key handling using environment variables.
- Added error handling for API failures and quota limitations.
- Used mock outputs as fallback when live API access was unavailable.

**Outcome:**  
Learned how prompt design impacts AI output and how to build robust systems that gracefully handle external API failures.

---

### TASK 5 – Mini AI System (Problem-First Design)

**Objective:**  
Design and implement a small AI-powered system for a real problem.

**Problem Chosen:**  
Student feedback analysis for educational institutions.

**Approach:**  
- Built an asynchronous FastAPI endpoint.
- Simulated AI-based sentiment analysis.
- Added a non-trivial logic layer using scoring and keyword-based fallback rules.
- Returned sentiment and priority scores for feedback.

**Outcome:**  
Demonstrated system-level thinking by combining AI logic, business rules, and backend APIs.

---

### TASK 6 – System Design & Deployment Concepts

**Objective:**  
Develop real-world system design understanding.

**Topics Covered:**  
- Monolith vs Microservices  
- Sync vs Async APIs  
- FastAPI with Uvicorn  
- Docker (conceptual)  
- API Security (API keys, rate limiting)

**Approach:**  
Explained where each concept should be used, where it should be avoided, and what issues arise if misused, supported by a simple architecture diagram.

---

## How to Run (For API Tasks)

1. Install dependencies:
pip install fastapi uvicorn


2. Run the FastAPI application:
uvicorn main:app --reload


3. Open Swagger UI:
http://127.0.0.1:8000/docs


---

## Key Learnings

- Real-world data is messy and requires preprocessing.
- Asynchronous APIs significantly improve performance under concurrency.
- Prompt engineering affects AI output quality.
- Robust systems require fallback handling.
- Design decisions are as important as implementation.

---

## Conclusion

This assignment provided hands-on exposure to real-world backend development, data analytics, AI integration, and system design concepts.  
It strengthened my problem-solving skills, system thinking, and understanding of scalable application design.

---

## Author

**Arpitha Singh: 23E51A6610**  

Undergraduate – Artificial Intelligence & Machine Learning  
Hyderabad Institute of Technology and Management (HITAM)
