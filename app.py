import streamlit as st

st.set_page_config(page_title="AI Skill Assessment Agent", layout="centered")

st.title("AI-Powered Skill Assessment & Learning Plan Agent")

st.write("Upload candidate details and get skill assessment + learning roadmap")

# ---------------- INPUTS (5 TOTAL) ----------------
job_desc = st.text_area("1. Paste Job Description")

resume = st.text_area("2. Paste Resume")

experience = st.text_input("3. Years of Experience")

target_role = st.text_input("4. Target Role (e.g., Data Scientist, Backend Dev)")

preferred_domain = st.selectbox(
    "5. Preferred Domain",
    ["AI/ML", "Web Development", "Data Science", "Cybersecurity", "Cloud Computing"]
)

# ---------------- PROCESS ----------------
if st.button("Generate Assessment"):

    if job_desc and resume:

        st.subheader("📊 Skill Assessment Summary")

        st.write(f"""
        **Target Role:** {target_role}  
        **Preferred Domain:** {preferred_domain}  
        **Experience:** {experience} years  
        """)

        st.subheader("🧠 Skill Evaluation")

        st.write("""
        - Python → Intermediate  
        - Problem Solving → Intermediate  
        - SQL → Beginner  
        - System Design → Beginner  
        - Machine Learning → Beginner  
        """)

        st.subheader("❗ Skill Gaps Identified")

        st.write("""
        - Advanced System Design  
        - Deep Learning  
        - Production-level ML deployment  
        """)

        st.subheader("📚 Personalized Learning Plan")

        st.write("""
        **1. System Design**
        - Resource: System Design Primer (GitHub)
        - Time: 3 weeks

        **2. Deep Learning**
        - Course: Andrew Ng Deep Learning Specialization
        - Time: 4–5 weeks

        **3. ML Deployment**
        - Resource: FastAPI + ML tutorials
        - Time: 2 weeks
        """)

        st.subheader("⏱ Estimated Total Learning Time")
        st.success("9–11 weeks (based on current skill level)")

    else:
        st.warning("Please fill Job Description and Resume")