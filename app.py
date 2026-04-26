import streamlit as st
import re

st.set_page_config(page_title="AI Skill Assessment Agent", layout="centered")

st.title("AI-Powered Skill Assessment & Learning Plan Agent")

st.write("Enter candidate details to generate a dynamic skill assessment and learning roadmap")

# ---------------- INPUTS ----------------
job_desc = st.text_area("1. Paste Job Description")

resume = st.text_area("2. Paste Resume")

experience = st.text_input("3. Years of Experience")

target_role = st.text_input("4. Target Role")

preferred_domain = st.selectbox(
    "5. Preferred Domain",
    ["AI/ML", "Web Development", "Data Science", "Cybersecurity", "Cloud Computing"]
)

# ---------------- HELPER FUNCTIONS ----------------

def extract_skills(text):
    """Simple keyword extraction from text"""
    common_skills = [
        "python", "java", "sql", "machine learning", "deep learning",
        "tensorflow", "pandas", "numpy", "react", "javascript",
        "html", "css", "linux", "docker", "aws", "system design"
    ]
    text = text.lower()
    return [skill for skill in common_skills if skill in text]

def get_proficiency(skill, exp):
    """Simulated proficiency based on experience"""
    if exp < 2:
        return "Beginner"
    elif exp < 5:
        return "Intermediate"
    else:
        return "Advanced"

# ---------------- MAIN LOGIC ----------------
if st.button("Generate Assessment"):

    if job_desc and resume:

        # convert experience safely
        try:
            exp = float(experience)
        except:
            exp = 0

        st.subheader("📊 Candidate Overview")
        st.write(f"**Experience:** {exp} years")
        st.write(f"**Target Role:** {target_role}")
        st.write(f"**Preferred Domain:** {preferred_domain}")

        # ---------------- SKILL EXTRACTION ----------------
        required_skills = extract_skills(job_desc)
        candidate_skills = extract_skills(resume)

        if not required_skills:
            required_skills = ["python", "problem solving", "communication"]

        st.subheader("🧠 Skill Match Analysis")

        matched = list(set(required_skills) & set(candidate_skills))
        missing = list(set(required_skills) - set(candidate_skills))

        match_score = int((len(matched) / len(required_skills)) * 100)

        st.write(f"**Skill Match Score:** {match_score}%")

        st.write("### Matched Skills")
        st.write(matched if matched else "None")

        st.write("### Missing Skills (Gaps)")
        st.write(missing if missing else "No major gaps")

        # ---------------- PROFICIENCY ----------------
        st.subheader("📈 Skill Proficiency")

        all_skills = list(set(required_skills + candidate_skills))

        for skill in all_skills:
            level = get_proficiency(skill, exp)
            st.write(f"- {skill.title()} → {level}")

        # ---------------- LEARNING PLAN ----------------
        st.subheader("📚 Personalized Learning Plan")

        if exp < 2:
            focus_level = "Foundational Learning Path"
        elif exp < 5:
            focus_level = "Intermediate Growth Path"
        else:
            focus_level = "Advanced Optimization Path"

        st.write(f"### {focus_level}")

        if missing:
            for skill in missing:
                st.write(f"""
                **{skill.title()}**
                - Learn basics → intermediate concepts
                - Build 1–2 small projects
                - Estimated time: 2–4 weeks
                """)
        else:
            st.write("Focus on advanced projects, system design, and real-world deployment.")

        # ---------------- TIME ESTIMATE ----------------
        base_time = len(missing) * 3

        if exp >= 5:
            base_time = max(2, base_time - 3)

        st.subheader("⏱ Estimated Learning Time")
        st.success(f"{base_time}–{base_time + 2} weeks")

    else:
        st.warning("Please fill Job Description and Resume")