# 🤖 Self-Learning AI Agent

> A self-learning AI agent built from scratch in Python that can understand goals, create plans, select tools, execute multi-step tasks, evaluate results, learn from experiences, and store reusable lessons in persistent memory.

🌐 **Live Demo:**  
https://self-learning-ai-agent.streamlit.app/

🐙 **GitHub Repository:**  
https://github.com/nirajkumar015/self-learning-ai-agent

---

## 🚀 Project Overview

This project is a goal-driven AI agent designed to demonstrate how autonomous AI systems can be built from scratch.

Unlike a simple chatbot that only generates responses, this agent can:

1. Understand a user's goal
2. Break the goal into logical steps
3. Decide which tool should be used
4. Execute the planned action
5. Observe the result
6. Evaluate whether the action succeeded
7. Learn a reusable lesson from the experience
8. Store the experience in memory
9. Use relevant previous experiences in future decisions

The core loop is:

```text
User Goal
    ↓
Planner
    ↓
Brain / LLM
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