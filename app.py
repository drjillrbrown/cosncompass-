import streamlit as st
import time

# Force wide mode to properly showcase the split-screen dashboard layout
st.set_page_config(layout="wide", page_title="CoSN PL AI Guide")

# SECURE CONFIGURATION: Pulling the credential safely from Streamlit's encrypted vault
if "cosn_api_key" not in st.session_state:
    if "COSN_API_KEY" in st.secrets:
        st.session_state["cosn_api_key"] = st.secrets["COSN_API_KEY"]
    else:
        st.session_state["cosn_api_key"] = "MOCK_MODE_ACTIVE"

# Initialize state flags and session records
if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "learning_path_data" not in st.session_state:
    st.session_state["learning_path_data"] = ""

def generate_mock_path(role, exp, size, focus, time_commit):
    """Generates the targeted framework plan matching all 5 user metrics."""
    return f"""
    ### 🗺️ Custom CoSN Learning Path
    
    **👤 Profile Metrics:**
    * **Role:** {role} ({exp})
    * **District Scope:** {size}
    * **Target Track:** {focus}
    * **Weekly Commitment Capacity:** {time_commit}
    
    ---
    #### 🚀 Phase 1: Foundation & Strategic Visioning
    * **Velocity Matrix:** Adjusted for *{time_commit}* Allocation.
    * **Action Items:** Review baseline CoSN resource infrastructure matching **{focus}** parameters.
    * **Resource Link:** [CoSN Professional Learning Framework](https://www.cosn.org)
    
    #### 🔒 Phase 2: Core Operational Implementation
    * **Operational Vector:** Tailored specifically for **{role}** leadership tracks within a **{size}**.
    * **Action Items:** Deep-dive into regional administrative guidelines and peer-tested toolkits.
    * **Resource Link:** [CoSN Member Tools & Assessment Resources](https://www.cosn.org)
    """

# --- UX Flow Component: Expanded Onboarding Assessment ---
if not st.session_state["form_submitted"]:
    st.title("🎯 Welcome to the CoSN PL AI Guide")
    st.subheader("Please complete your professional baseline profile to customize your roadmap:")
    
    with st.form("intake_form"):
        # Question 1
        role = st.selectbox(
            "1. What is your current educational leadership role?", 
            [
                "Chief Technology Officer (CTO) / Chief Information Officer (CIO)",
                "Director of Technology / Technology Coordinator",
                "Superintendent / Assistant Superintendent",
                "Instructional Technology Coach / Specialist",
                "Network Administrator / Cybersecurity Specialist",
                "Other Education Stakeholder"
            ]
        )
        
        # Question 2
        exp = st.selectbox(
            "2. How many years of experience do you have in this role?",
            [
                "New to the role (0-2 years)",
                "Mid-career professional (3-5 years)",
                "Seasoned veteran (6+ years)"
            ]
        )
        
        # Question 3
        size = st.selectbox(
            "3. What size is your school district?",
            [
                "Small District (Fewer than 2,500 students)",
                "Medium District (2,500 – 10,000 students)",
                "Large District (More than 10,000 students)"
            ]
        )
        
        # Question 4
        focus = st.selectbox(
            "4. What are your primary focus areas for professional growth right now?",
            [
                "Strategic Leadership, District Visioning & Stakeholder Communication",
                "IT Management, Budgeting & Infrastructure",
                "CETL® Certification Exam Preparation & Foundation Review",
                "Cybersecurity Planning, Risk Assessments & Frameworks",
                "Incident Response & Tabletop Exercises"
            ]
        )
        
        # Question 5
        time_commit = st.selectbox(
            "5. How much time can you realistically commit to learning each week?",
            [
                "1 Hour per week (Quick reference tools & checklists)",
                "2-3 Hours per week (Focused webinar series & brief workshops)",
                "4-5 Hours per week (In-depth structured courses & tabletop exercises)",
                "5+ Hours per week (Comprehensive pathways & leadership modules)"
            ]
        )
        
        # Native Streamlit form execution button
        submit_button = st.form_submit_button("Generate My Guide")
        
        if submit_button:
            st.session_state["learning_path_data"] = generate_mock_path(role, exp, size, focus, time_commit)
            
            initial_greeting = (
                f"Hello! I've cataloged your profile as a **{role}** ({exp}) managing a **{size}**. "
                f"Your customized training path focusing on **{focus}** has been built on your right dashboard panel. "
                f"How can I assist you with your weekly target of **{time_commit}** today?"
            )
            st.session_state["chat_history"].append({"role": "assistant", "content": initial_greeting})
            st.session_state["form_submitted"] = True
            st.rerun()

# --- The Layout: Split-Screen Dashboard UI ---
else:
    left_col, right_col = st.columns([1, 1], gap="large")
    
    # Left Column: Dynamic Chat Interface
    with left_col:
        st.header("💬 AI Assistant Chat")
        
        # Render historical chat records safely
        for message in st.session_state["chat_history"]:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Listen for new multi-turn interactions
        if user_prompt := st.chat_input("Ask a follow-up question..."):
            with st.chat_message("user"):
                st.markdown(user_prompt)
            st.session_state["chat_history"].append({"role": "user", "content": user_prompt})
            
            # Simulate processing delay
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                response_placeholder.markdown("*Searching CoSN specifications...*")
                time.sleep(0.8)
                mock_reply = f"I've processed your question regarding '{user_prompt}'. We suggest referencing the operational toolkits on the right panel to execute this strategy effectively."
                response_placeholder.markdown(mock_reply)
            
            st.session_state["chat_history"].append({"role": "assistant", "content": mock_reply})

    # Right Column: Scannable/Printable Learning Path View
    with right_col:
        st.header("📋 Your Custom Learning Path")
        st.info("💡 Pro-Tip: You can print this layout directly from your browser menu (Ctrl+P / Cmd+P).")
        st.markdown(st.session_state["learning_path_data"])
        
        if st.button("Reset / New Profile Intake"):
            st.session_state["form_submitted"] = False
            st.session_state["chat_history"] = []
            st.session_state["learning_path_data"] = ""
            st.rerun()