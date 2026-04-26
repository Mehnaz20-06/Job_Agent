import streamlit as st
import os
from openai import OpenAI

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Skill Assessment Agent", layout="centered")

st.title("AI-Powered Skill Assessment & Learning Plan Agent")
st.write("Hybrid AI system (LLM + fallback logic)")

# ---------------- OPENAI CLIENT ----------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------- INPUTS ----------------
job_desc = st.text_area("1. Paste Job Description")
resume = st.text_area("2. Paste Resume")
experience = st.text_input("3. Years of Experience")
target_role = st.text_input("4. Target Role")
preferred_domain = st.selectbox(
    "5. Preferred Domain",
    ["AI/ML", "Web Development", "Data Science", "Cybersecurity", "Cloud Computing"]
)

# ---------------- FALLBACK LOGIC ----------------
def rule_based_output(exp, domain):
    try:
        exp = float(exp)
    except:
        exp = 0

    # domain skills map
    domain_skills = {
        "AI/ML": ["Python", "Machine Learning", "Deep Learning", "Statistics"],
        "Web Development": ["HTML", "CSS", "JavaScript", "React"],
        "Data Science": ["Python", "Pandas", "SQL", "Visualization"],
        "Cybersecurity": ["Networking", "Linux", "Ethical Hacking"],
        "Cloud Computing": ["AWS", "Docker", "Linux", "CI/CD"]
    }

    skills = domain_skills.get(domain, ["Programming Basics"])

    match_score = max(40, min(95, int(exp * 15)))

    if exp < 2:
        level = "Beginner Profile"
    elif exp < 5:
        level = "Intermediate Profile"
    else:
        level = "Advanced Profile"

    gaps = skills[-2:] if exp < 3 else skills[-1:] if exp < 5 else []

    learning_plan = []
    for g in gaps:
        learning_plan.append(f"{g} → 2-3 weeks learning + mini project")

    return {
        "level": level,
        "match": match_score,
        "skills": skills,
        "gaps": gaps,
        "plan": learning_plan
    }

# ---------------- MAIN ----------------
if st.button("Generate Assessment"):

    if job_desc and resume:

        st.subheader("📊 Processing Candidate Data...")

        # -------- TRY AI FIRST --------
        try:
            prompt = f"""
You are an AI career advisor.

Analyze:

Job Description:
{job_desc}

Resume:
{resume}

Experience: {experience}
Target Role: {target_role}
Preferred Domain: {preferred_domain}

Return:
- Skill match %
- Required skills
- Candidate skills
- Gaps
- Proficiency per skill
- Learning plan
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert AI career advisor."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content

            st.success("AI-powered output (OpenAI)")
            st.markdown(result)

        # -------- FALLBACK IF API FAILS --------
        except:
            st.warning("AI quota unavailable → using rule-based system")

            exp = experience
            data = rule_based_output(exp, preferred_domain)

            st.subheader("📊 Skill Match Score")
            st.success(f"{data['match']}%")

            st.subheader("🧠 Candidate Level")
            st.write(data["level"])

            st.subheader("📌 Required Skills")
            st.write(data["skills"])

            st.subheader("❗ Skill Gaps")
            st.write(data["gaps"] if data["gaps"] else "No major gaps")

            st.subheader("📚 Personalized Learning Plan")
            for item in data["plan"]:
                st.write("- " + item)

            st.subheader("⏱ Estimated Learning Time")
            st.success("6–10 weeks depending on pace")

    else:
        st.warning("Please fill Job Description and Resume")