# 🦙 LangChain + Ollama + Streamlit Demo

This project demonstrates how to run LLaMA2 locally using [Ollama](https://ollama.com/) and interact with it via a simple [Streamlit](https://streamlit.io/) interface powered by [LangChain](https://www.langchain.com/). It’s designed for developers who want a lightweight, local LLM experience with prompt chaining and UI integration.

---

## 📦 Features

- 🔗 LangChain prompt orchestration and output parsing
- 🧠 Local LLaMA2 model served via Ollama
- 🖥️ Interactive Streamlit frontend
- 🔍 Optional LangChain tracing for observability
- 🔐 Environment-based configuration using `.env`

---

## 🧰 Requirements

- Python 3.10+
- [Ollama installed locally](https://ollama.com/download)
- LLaMA2 model pulled via Ollama:
  ```bash
  ollama pull llama3
