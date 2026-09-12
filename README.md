\# Self-Learning AI Agent 🤖



A self-learning AI agent built from scratch in Python using a local LLM through Ollama.



The agent can understand goals, create plans, select tools, execute actions, evaluate results, learn lessons from experiences, and store those lessons in persistent memory.



\## 🧠 Architecture



User Goal

&#x20;  ↓

Agent Controller

&#x20;  ↓

Planner

&#x20;  ↓

Brain / LLM

&#x20;  ↓

Tool Selection

&#x20;  ↓

Action

&#x20;  ↓

Observation

&#x20;  ↓

Evaluation

&#x20;  ↓

Learner

&#x20;  ↓

Persistent Memory

&#x20;  ↓

Future Decisions



\## ✨ Features



\- Goal-based task execution

\- AI-powered planning

\- Local LLM using Ollama

\- AI-driven tool selection

\- Calculator tool

\- Python execution tool

\- File read/write tools

\- Persistent JSON memory

\- Relevant memory retrieval

\- Experience evaluation

\- Automatic lesson extraction

\- Learning from previous experiences

\- Step retry and error recovery

\- Multi-step autonomous task execution



\## 🛠️ Tech Stack



\- Python 3.11

\- Ollama

\- Qwen3 4B

\- JSON

\- PowerShell / Windows

\- VS Code



\## 📁 Project Structure



```text

self\_learning\_agent/

│

├── agent.py

├── brain.py

├── planner.py

├── learner.py

├── memory.py

├── final\_response.py

├── main.py

├── experiences.json

├── requirements.txt

├── .gitignore

│

├── tools/

│   ├── \_\_init\_\_.py

│   ├── calculator.py

│   ├── python\_tool.py

│   └── file\_tool.py

│

└── venv/

