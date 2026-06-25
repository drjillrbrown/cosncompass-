import streamlit as st
import time

# Force wide mode to properly showcase the split-screen dashboard layout
st.set_page_config(layout="wide", page_title="CoSN PL AI Guide")

# SECURE CONFIGURATION: Pulling the credential safely from Streamlit's encrypted vault
if "cosn_api_key" not in st.session_state:
    if "COSN_API_KEY" in st.secrets:
        st.session_state["cosn_api_key"] = st.secrets["COSN_API_KEY"]
    else:
        # Fallback to keep the app functional locally or if the secret isn't configured yet
        st.session_state["cosn_api_key"] = "MOCK_MODE_ACTIVE"

# Initialize state flags and mock database
if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "learning_path_data" not in st.session_state:
    st.session_state["learning_path_data"] = ""

def generate_mock_path(role, size, goal):
    """Simulates the architecture's Option 1 mock API response."""
    return f"""
    ### 🗺️ Custom Learning Path for {role}
    **District Profile:** {size} | **Primary Focus:** {goal}
    
    ---
    #### 🚀 Phase 1: Foundation & Alignment
    * **Time Commitment:** 2-3 Hours (Week 1)
    * **Action Items:** Review CoSN Framework essentials tailored for your dynamic goals.
    * **Resource:** [CoSN Core Framework Resource Link](https://www.cosn.org)
    
    #### 🔒 Phase 2: Implementation & Risk Assessment
    * **Time Commitment:** 5 Hours (Weeks 2-3)
    * **Action Items:** Conduct initial system diagnostics based on standard security vectors.
    * **Resource:** [CoSN Cybersecurity Toolkit](https://www.cosn.org)
    """

# --- UX Flow Component: 3-Question Intake Form ---
if not st.session_state["form_submitted"]:
    st.title("🎯 Welcome to the CoSN PL AI Guide")
    st.subheader("Let's quick-start your experience. Tell us about your profile:")
    
    with st.form("intake_form"):
        role = st.selectbox("1. What is your primary Role?", ["Superintendent", "CTO / Technology Director", "Instructional Coach", "District Administrator"])
        size = st.selectbox("2. What is your District Size?", ["Small (Under 3,000 students)", "Medium (3,000 - 10,000 students)", "Large (10,000+ students)"])
        goal = st.selectbox("3. What is your Primary Goal?", ["Cybersecurity Strategy", "Data Privacy Frameworks", "Superintendent Tools Implementation"])
        
        # Fixed native Streamlit form submission handler
        submit_button = st.form_submit_button("Generate My Guide")
        
        if submit_button:
            st.session_state["learning_path_data"] = generate_mock_path(role, size, goal)
            st.session_state["chat_history"].append({"role": "assistant", "content": f"Hello! I've analyzed your profile as a **{role}** handling a **{size}** district. I have customized your learning path on the right dashboard pane. How else can I assist you with **{goal}** today?"})
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
                mock_reply = f"I've evaluated your point regarding '{user_prompt}'. According to standard CoSN protocols, you should align this with your current infrastructure baseline."
                response_placeholder.markdown(mock_reply)
            
            st.session_state["chat_history"].append({"role": "assistant", "content": mock_reply})

    # Right Column: Scannable/Printable Learning Path View
    with right_col:
        st.header("📋 Your Custom Learning Path")
        st.info("💡 Pro-Tip: You can print this dashboard layout directly from your browser menu (Ctrl+P / Cmd+P).")
        st.markdown(st.session_state["learning_path_data"])
        
        if st.button("Reset / New Profile Intake"):
            st.session_state["form_submitted"] = False
            st.session_state["chat_history"] = []
            st.session_state["learning_path_data"] = ""
            st.rerun()