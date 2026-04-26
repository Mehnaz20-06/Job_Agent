import streamlit as st

st.title("AI Skill Assessment Agent")

st.write("Evaluate candidate skills and generate a personalized learning plan")

# Inputs
job_desc = st.text_area("Paste Job Description")
resume = st.text_area("Paste Resume")
experience = st.text_input("Years of Experience")

if st.button("Assess Candidate"):

    if job_desc and resume:
        # Mock AI output (safe for demo)
        st.subheader("Skill Assessment")

        st.write("""
        **Python:** Intermediate  
        **Machine Learning:** Beginner  
        **SQL:** Intermediate  
        """)

        st.subheader("Skill Gaps")
        st.write("""
        - Deep Learning  
        - System Design  
        """)

        st.subheader("Personalized Learning Plan")
        st.write("""
        **Deep Learning**
        - Course: Andrew Ng Specialization  
        - Time: 4 weeks  

        **System Design**
        - Resource: System Design Primer  
        - Time: 3 weeks  
        """)

    else:
        st.warning("Please fill all inputs")