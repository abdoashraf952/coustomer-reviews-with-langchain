# 📊 AI Customer Reviews Intelligence System

An end-to-end AI system that automatically analyzes customer feedback, detects recurring problems, evaluates their severity, and suggests actionable solutions — all visualized in a live dashboard.

This project combines Sentiment Analysis, LLM problem extraction, FastAPI, Ngrok, Google Sheets, and Streamlit into one intelligent pipeline.

---

## 🧠 System Overview

Flow:

1. Customer submits feedback → Streamlit form
2. Feedback stored in → Google Sheet
3. AI pipeline reads reviews → filters negative ones
4. LLM extracts the main problem
5. System counts recurring problems
6. LLM generates:
   - Problem
   - Number of occurrences
   - Severity (1–5)
   - Suggested solution
7. Results exposed via API
8. Dashboard visualizes insights

---

## 🚀 Features

- Automatic negative review detection
- LLM-based problem extraction
- Recurring issue detection
- AI severity assessment
- AI resolution plan
- Live API with FastAPI
- Public access via ngrok
- Streamlit analytics dashboard
- Streamlit feedback form (live data collection)

---

## 🛠️ Tech Stack

- DistilBERT (Sentiment Analysis)
- Mistral-Nemo-Instruct-2407 (LLM)
- LangChain
- FastAPI
- ngrok
- Streamlit
- Google Sheets
- Pandas

---

## 📁 Project Structure

```
├── coustomer_reviews.ipynb
├── dashboad_GUI.py
├── feedback_GUI.py
├── credentials.json
└── README.md
```
---

## ⚙️ How It Works

### 1) Feedback Collection

streamlit run feedback_GUI.py

### 2) Start AI API

Open and run all cells in:

coustomer_reviews.ipynb

You will receive a public URL like:

https://xxxxx.ngrok-free.dev/show_reviews

### 3) Start Dashboard

streamlit run dashboad_GUI.py

Click **Start Analysis** to view insights.

---

## 🔑 Installation

pip install transformers==4.53.3 langchain gspread google-auth pandas fastapi uvicorn pyngrok accelerate streamlit

---

## 🧾 Example Output

{
  "Problem": "Late delivery",
  "Number of occurrences": 18,
  "Severity level": 4,
  "Suggested Solution": "Improve delivery routing and notify customers proactively."
}

---

## 🎯 Use Cases

- E-commerce platforms
- Customer support monitoring
- Service quality tracking
- CX analytics automation
- Product issue discovery

---

## 👨‍💻 Author

Abdelrhman Ashraf  
Faculty of Engineering — Computers & Systems

