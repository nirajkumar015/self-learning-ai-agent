# 🤖 Self-Learning AI Agent

> A self-learning AI agent built from scratch in Python that can understand goals, create plans, select tools, execute multi-step tasks, evaluate results, learn from experiences, and store reusable lessons in memory.

🌐 **Live Demo:**  
https://self-learning-ai-agent.streamlit.app/

🐙 **GitHub Repository:**  
https://github.com/nirajkumar015/self-learning-ai-agent

---

## 🚀 Project Overview

This project is a goal-driven AI agent built from scratch using Python.

Unlike a simple chatbot that only generates answers, this agent can:

1. Understand a user's goal
2. Break the goal into smaller steps
3. Decide which tool should be used
4. Execute the planned action
5. Observe the result
6. Check whether the action succeeded
7. Learn a useful lesson from the experience
8. Store the experience in memory
9. Use relevant previous experiences in future tasks

The main idea is to combine an LLM with normal Python code, tools, memory, planning, and evaluation.

---

## 🧠 How the Agent Works

The basic flow is:

```text
User Goal
    ↓
Planner
    ↓
Brain / LLM
    ↓
Gemini API / Ollama + Qwen3
    ↓
Tool Selection
    ↓
Action
    ↓
Observation
    ↓
Evaluation
    ↓
Learner
    ↓
Memory
    ↓
Future Decisions
