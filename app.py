import streamlit as st
import time

# 1. Force wide mode instantly before executing any secondary properties
st.set_page_config(layout="wide", page_title="CoSN PL AI Guide")

# 2. Complete, Production-Grade Media Catalog Schema
MULTIMODAL_COSN_CATALOG = {
    "Cybersecurity & Incident Response": [
        {
            "phase": "1. Foundations (Course)",
            "title": "CoSN Cybersecurity in K-12 Schools Facilitated Online Course",
            "url": "https://www.cosn.org/education-events/online-courses/",
            "duration": "7 weeks (1 live hour/week)",
            "why": "Establishes foundational enterprise security competencies, covering networks, risks, and threat mitigations specifically for K-12 IT staff."
        },
        {
            "phase": "2. Intermediate (Workshop & Toolkit)",
            "title": "Cyber Resilience Blueprint: Building Your District's Security & Incident Response Plans",
            "url": "https://www.cosn.org/courses-workshops-catalog/",
            "duration": "3-hour Live Interactive Event",
            "why": "Moves you from theory to execution. You will actively build out your district's business continuity and tabletop simulation framework."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "Quick Wins: Cybersecurity Scalable Solutions for Districts of Any Size",
            "url": "https://www.cosn.org/edtech-topic/webinar-recording/",
            "duration": "45-minute Briefing / Audio Podcast",
            "why": "Provides immediate, low-overhead tactical changes that technology leaders can implement instantly to protect infrastructure with minimal budget."
        }
    ],
    "Student Data Privacy & AI Governance": [
        {
            "phase": "1. Foundations (Course)",
            "title": "CoSN Trusted Learning Environment (TLE) Self-Directed Online Course",
            "url": "https://www.cosn.org/year-round-catalog/",
            "duration": "Self-paced (Approx. 4 hours)",
            "why": "Unpacks the 5 core practice areas required to safeguard student records and lays the groundwork for earning the national TLE privacy seal."
        },
        {
            "phase": "2. Intermediate (Workshop)",
            "title": "Privacy & AI: Striking the Balance in Schools Facilitated Online Workshop",
            "url": "https://www.cosn.org/courses-workshops-catalog/",
            "duration": "3 hours total",
            "why": "Addresses vendor SaaS procurement issues and outlines specific policy guardrails for safe generative AI implementation inside classrooms."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "Managing Student Data Privacy: Highlights of the National Student Data Privacy Report",
            "url": "https://www.cosn.org/edtech-topic/webinar-recording/",
            "duration": "1-hour Panel Recording & Podcast",
            "why": "A panel of active superintendents and CTOs sharing real-world compliance successes and legal hurdles under FERPA/COPPA updates."
        }
    ]
}

# 3. Secure Fallback Routine for Memory Stream Alignment
if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "learning_path_data" not in st.session_state:
    st.session_state["learning_path_data"] = ""
if "selected_focus" not in st.session_state:
    st.session_state["selected_focus"] = list(MULTIMODAL_COSN_CATALOG.keys())[0]

def build_multimodal_path(role, exp, size, focus, time_commit):
    suggestions = MULTIMODAL_COSN_CATALOG.get(focus, [])
    md_output = f"""
### 🗺️ Your Customized CoSN Multi-Format Learning Path

**👤 Leadership Profile Summary:**
* **Role/Context:** {role} ({exp})
* **District Footprint:** {size}
* **Realistic Commitment:** {time_commit}
* **Primary Track Target:** {focus}

---
### 🎓 Your 3-Step Media Ecosystem Roadmap
"""
    for item in suggestions:
        md_output += f"""
#### **📍 Phase {item['phase']}**
* **Resource:** [{item['title']}]({item['url']})
* **Time Commitment:** {item['duration']}
* **Strategic Context:** {item['why']}
"""
    return md_output

def generate_catalog_response(user_query, current_focus):
    query_lower = user_query.lower()
    suggestions = MULTIMODAL_COSN_CATALOG.get(current_focus, [])
    if any(k in query_lower for k in ["cabinet", "board", "superintendent", "involve", "engage"]):
        return f"### 🏛️ Cabinet Engagement Strategy ({current_focus}):\n\nTo engage leadership, introduce: **\"{suggestions[1]['title']}\"**. Framing this as an asset protection measure rather than an IT task ensures stakeholder buy-in."
    return f"### 📋 Catalog Cross-Reference:\n\nReview your active dashboard menu selections to coordinate training modules."

# 4. Interface Presentation Layer
if not st.session_state["form_submitted"]:
    st.title("🎯 Welcome to the CoSN PL AI Guide")
    with st.form("intake_form"):
        role = st.selectbox("1. What is your current educational leadership role?", ["Chief Technology Officer (CTO) / Chief Information Officer (CIO)", "Director of Technology / Technology Coordinator"])
        exp = st.selectbox("2. How many years of experience do you have in this role?", ["New to the role (0-2 years)", "Seasoned veteran (6+ years)"])
        size = st.selectbox("3. What size is your school district?", ["Small District (Fewer than 2,500 students)", "Large District (More than 10,000 students)"])
        focus = st.selectbox("4. What are your primary focus areas for professional growth right now?", list(MULTIMODAL_COSN_CATALOG.keys()))
        time_commit = st.selectbox("5. How much time can you realistically commit to learning each week?", ["1 Hour per week", "5+ Hours per week"])
        
        if st.form_submit_button("Generate My Guide"):
            st.session_state["selected_focus"] = focus
            st.session_state["learning_path_data"] = build_multimodal_path(role, exp, size, focus, time_commit)
            st.session_state["chat_history"].append({"role": "assistant", "content": f"Calibrated for **{focus}**. Let's begin optimization."})
            st.session_state["form_submitted"] = True
            st.rerun()
else:
    left_col, right_col = st.columns([1, 1], gap="large")
    with left_col:
        st.header("💬 AI Assistant Chat")
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if user_prompt := st.chat_input("Ask a follow-up question..."):
            with st.chat_message("user"): st.markdown(user_prompt)
            st.session_state["chat_history"].append({"role": "user", "content": user_prompt})
            with st.chat_message("assistant"):
                reply = generate_catalog_response(user_prompt, st.session_state["selected_focus"])
                st.markdown(reply)
            st.session_state["chat_history"].append({"role": "assistant", "content": reply})
    with right_col:
        st.header("📋 Your Custom Learning Path")
        st.markdown(st.session_state["learning_path_data"])
        if st.button("Reset Profile"):
            st.session_state["form_submitted"] = False
            st.session_state["chat_history"] = []
            st.session_state["learning_path_data"] = ""
            st.rerun()