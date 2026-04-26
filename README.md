# AI-Powered Skill Assessment & Personalized Learning Plan Agent

## 📌 Project Overview

A resume tells you what a candidate *claims* to know — but not how well they actually understand it.

This project is a **rule-based AI agent prototype** that takes a Job Description and a Candidate Resume, evaluates skills, identifies gaps, and generates a personalized learning roadmap based on experience, role, and domain preference.

It demonstrates how AI systems can be designed for skill evaluation and adaptive learning recommendations.

---

## 🚀 Live Demo


Example:
https://jobagent-cr78jepwmjlfrsrizappajo.streamlit.app/
---

## 🎯 Features

- Accepts multiple user inputs (5 inputs total)
- Extracts and evaluates candidate skill level (simulated logic)
- Identifies skill gaps based on target role
- Generates personalized learning roadmap
- Estimates learning duration
- Domain-aware recommendations (AI/ML, Cybersecurity, etc.)

---

## 🧠 Inputs

1. Job Description  
2. Resume  
3. Years of Experience  
4. Target Role  
5. Preferred Domain  

---

## 📤 Outputs

- Skill Assessment Summary  
- Skill Evaluation Breakdown  
- Identified Skill Gaps  
- Personalized Learning Plan  
- Estimated Learning Time  

---

## ⚙️ System Architecture
User Inputs → Streamlit UI → Rule-Based Logic Engine → Output Generation → Display

---

## 🧩 Tech Stack

- Python
- Streamlit
- Rule-based logic engine (no external API required)

---

## 🧠 Working Principle

The system uses conditional logic to simulate AI behavior:

- Adjusts skill evaluation based on domain
- Modifies learning paths based on experience level
- Generates structured learning recommendations

This makes it a **prototype of an AI-driven career guidance agent**.

---



## 💡 Future Improvements

- Integration with Large Language Models for real reasoning
- Resume parsing using NLP
- Real-time skill scoring system
- Personalized adaptive learning feedback loop

---

## 🔮 Bonus Insight

In production, this logic can be replaced with an LLM for deeper semantic reasoning

---

## ▶️ How to Run Locally

```bash
pip install streamlit
streamlit run app.py
