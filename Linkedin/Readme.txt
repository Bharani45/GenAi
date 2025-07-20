# 🤖 LinkedIn Post Generator

This is a simple yet powerful **LinkedIn Post Generator** built using **Streamlit**, **LangChain**, and **LLM APIs** (e.g., Groq with LLaMA 3). It allows users to generate context-aware LinkedIn posts based on selected **topic**, **language**, **length**, and **tone**.

---

## 🚀 Features

- 🔍 Choose from various topics like Productivity, Mental Health, Leadership, etc.
- 🗣 Select the tone: Professional, Casual, Funny
- 📝 Customize post length: Short, Medium, Long
- 🌐 Choose between English and Hinglish
- 💬 Instant AI-generated posts using LLM
- 💾 Download post as `.txt`
- ⭐ Submit feedback using a rating slider (saved in `feedback.json`)
- 🧠 Few-shot learning to match tone and format using sample posts

---

## 🧰 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [LLaMA 3 via Groq API](https://groq.com/)
- [dotenv](https://pypi.org/project/python-dotenv/)
- [Pandas](https://pandas.pydata.org/)

---

## 📁 Project Structure

```bash
.
├── data/
│   ├── raw_posts.json
│   └── processed_posts.json
├── feedback.json
├── main.py                # Streamlit frontend
├── few_shot.py            # Few-shot examples manager
├── post_generator.py      # Prompt + LLM interaction
├── llm_helper.py          # LLM API setup (Groq/LangChain)
├── .env                   # API keys
└── README.md

#Demo-https://drive.google.com/drive/folders/11R_H9yBeh5uqwmb4-w8XZM5SbOyhRtdV?usp=drive_link

