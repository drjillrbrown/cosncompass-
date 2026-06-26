import streamlit as st
import time

# Force wide mode instantly before executing any secondary properties
st.set_page_config(layout="wide", page_title="CoSN PL AI Guide")

# --- Height Optimization: Strip default whitespace padding ---
st.markdown("""
    <style>
        .block-container {padding-top: 1rem !important; padding-bottom: 0rem !important;}
        div[data-testid="stForm"] {margin-top: 0rem !important; padding-top: 1rem !important;}
        h1 {margin-bottom: 0rem !important; padding-bottom: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

# --- Production Data Layer: Full 5-Track Catalog with Verified Deep Links ---
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
            "url": "https://www.cosn.org/event/cyber-resilience-blueprint-building-your-districts-security-incident-response-plans-fall-2026/",
            "duration": "3-hour Live Interactive Event",
            "why": "Moves you from theory to execution. This deep-link directs users directly to the active workshop registration and syllabus portal."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "CoSN Member Resource: 2026 State of EdTech Leadership National Report & Briefing",
            "url": "https://www.cosn.org/wp-content/uploads/2026/05/U.S.-State-of-EdTech-2026.pdf",
            "duration": "Downloadable Briefing / Audio Overview Available",
            "why": "Provides immediate, macro-level benchmarking data on national cybersecurity constraints, direct from the 2026 published index."
        }
    ],
    "Student Data Privacy & AI Governance": [
        {
            "phase": "1. Foundations (Course)",
            "title": "CoSN Trusted Learning Environment (TLE) Self-Directed Online Course",
            "url": "https://www.cosn.org/education-events/online-courses/",
            "duration": "Self-paced (Approx. 4 hours)",
            "why": "Direct track to the TLE course segment detailing the 5 practice areas required to protect district student data systems."
        },
        {
            "phase": "2. Intermediate (Workshop & Interactive Tool)",
            "title": "CoSN K-12 Gen AI Maturity Tool & AI Advisor Interactive Diagnostic",
            "url": "https://www.cosn.org/ai/",
            "duration": "Collaborative Team Session",
            "why": "Brings the user directly to the live 2026 interactive advisor dashboard to move school cabinets from abstract ideas to operational guardrails."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "Trusted Learning Environment Application & National Benchmarking Framework",
            "url": "https://www.cosn.org/trusted-learning-environment-faqs/",
            "duration": "1-hour Implementation Review",
            "why": "Deep link to the explicit blueprint criteria needed to compile the final district privacy portfolio to earn the TLE stamp."
        }
    ],
    "Strategic Leadership, District Visioning & Stakeholder Communication": [
        {
            "phase": "1. Foundations (Course)",
            "title": "CETL® K-12 CTO's Framework of Essential Skills Foundation Course",
            "url": "https://www.cosn.org/education-events/online-courses/",
            "duration": "8 weeks",
            "why": "Provides the foundational competencies required to lead systemic EdTech initiatives across districts."
        },
        {
            "phase": "2. Intermediate (Workshop & Toolkit)",
            "title": "CoSN Member Tools & Assessment Resources Portal",
            "url": "https://www.cosn.org/tools-resources/",
            "duration": "Self-Directed Download",
            "why": "Peer-tested administrative frameworks and stakeholder slide-decks to cleanly align your executive team."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "EdTech Leadership Trends: Driving Multi-Department Communication",
            "url": "https://www.cosn.org/education-events/webinars/",
            "duration": "1-hour Briefing",
            "why": "Focuses on strategic marketing and language translations needed to pitch complex infrastructure changes to your local board."
        }
    ],
    "IT Management, Budgeting & Infrastructure": [
        {
            "phase": "1. Foundations (Course)",
            "title": "Unlocking Value of Investment (VOI) and Total Cost of Ownership (TCO) for EdTech Leaders",
            "url": "https://www.cosn.org/education-events/online-courses/",
            "duration": "2-week Workshop",
            "why": "Crucial for budgeting and hardware/software lifecycle management within your district infrastructure."
        },
        {
            "phase": "2. Intermediate (Workshop & Toolkit)",
            "title": "CoSN TCO and VOI Pricing Calculators & Implementation Manual",
            "url": "https://www.cosn.org/tools-resources/",
            "duration": "Interactive Toolkit",
            "why": "Directly guides you through formal capital planning spreadsheets to calculate accurate device lifecycle costs."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "Smart Budgeting: Preserving Classroom Tech Equity in Tight Fiscal Waves",
            "url": "https://www.cosn.org/education-events/webinars/",
            "duration": "45-minute Panel",
            "why": "Active operational strategies to defend your technical infrastructure investments during local budget contractions."
        }
    ],
    "CETL® Certification Exam Preparation & Foundation Review": [
        {
            "phase": "1. Foundations (Course)",
            "title": "CoSN Certified Education Chief Technology Officer (CETL) Certification Program",
            "url": "https://www.cosn.org/certification/",
            "duration": "Self-Paced or Cohort",
            "why": "The premier national credential demonstrating absolute mastery of the K-12 EdTech leadership matrix."
        },
        {
            "phase": "2. Intermediate (Workshop & Toolkit)",
            "title": "CETL® Examination Content Domain Review & Study Guide",
            "url": "https://www.cosn.org/certification/prepare-for-cetl/",
            "duration": "Comprehensive Manual",
            "why": "Provides exact framework breakdowns for the three core leadership domains tested on the exam."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "The Road to the CETL: Tips and Strategies from Newly Certified Leaders",
            "url": "https://www.cosn.org/education-events/webinars/",
            "duration": "1-hour Community Recording",
            "why": "Veteran study tips, preparation timeline schedules, and test-taking advice from recent certified designees."
        }
    ]
}

# Secure Fallback Routine for Memory Stream Alignment
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
    
    md_output = "### 🗺️ Your Customized CoSN Multi-Format Learning Path\n\n"
    md_output += f"* **Role/Context:** {role}\n"
    md_output += f"* **Experience Level:** {exp}\n"
    md_output += f"* **District Footprint:** {size}\n"
    md_output += f"* **Realistic Commitment:** {time_commit}\n"
    md_output += f"* **Primary Track Target:** {focus}\n\n"
    md_output += "---\n### 🎓 Your 3-Step Media Ecosystem Roadmap\n\n"
    
    for item in suggestions:
        md_output += f"#### 📍 Phase {item['phase']}\n"
        md_output += f"* **Resource:** [{item['title']}]({item['url']})\n"
        md_output += f"* **Time Commitment:** {item['duration']}\n"
        md_output += f"* **Strategic Context:** {item['why']}\n\n"
    return md_output

def generate_catalog_response(user_query, current_focus):
    query_lower = user_query.lower()
    suggestions = MULTIMODAL_COSN_CATALOG.get(current_focus, [])
    
    if not suggestions or len(suggestions) < 3:
        return "### 📋 Profile Alignment Reference:\nI am calibrated to use our curated multi-format data catalog to assist you."

    if any(k in query_lower for k in ["cabinet", "board", "superintendent", "involve", "engage"]):
        resp = f"### 🏛️ Cabinet Engagement Strategy ({current_focus}):\n\n"
        resp += f"To effectively engage your executive leadership on this track, introduce the intermediate resource: **\"{suggestions[1]['title']}\"**. "
        resp += f"Framing this to your cabinet as an asset protection measure ensures baseline alignment."
        return resp
        
    fallback = f"### 📋 Catalog Cross-Reference:\n\n"
    fallback += f"Regarding your query on '{user_query}', your active **{current_focus}** track provides structural support via three distinct formats:\n"
    fallback += f"* **Course:** {suggestions[0]['title']} ({suggestions[0]['duration']})\n"
    fallback += f"* **Workshop:** {suggestions[1]['title']} ({suggestions[1]['duration']})\n"
    fallback += f"* **Webinar/Audio:** {suggestions[2]['title']} ({suggestions[2]['duration']})\n\n"
    return fallback

# Interface Presentation Layer
if not st.session_state["form_submitted"]:
    st.title("🎯 Welcome to the CoSN PL AI Guide")
    st.subheader("Please complete your professional baseline profile to customize your roadmap:")
    with st.form("intake_form"):
        role = st.selectbox("1. What is your current educational leadership role?", [
            "Chief Technology Officer (CTO) / Chief Information Officer (CIO)", 
            "Director of Technology / Technology Coordinator",
            "Superintendent / Assistant Superintendent",
            "Instructional Technology Coach / Specialist",
            "Network Administrator / Cybersecurity Specialist",
            "Other Education Stakeholder"
        ])
        exp = st.selectbox("2. How many years of experience do you have in this role?", [
            "New to the role (0-2 years)", 
            "Mid-career professional (3-5 years)", 
            "Seasoned veteran (6+ years)"
        ])
        size = st.selectbox("3. What size is your school district?", [
            "Small District (Fewer than 2,500 students)", 
            "Medium District (2,500 – 10,000 students)", 
            "Large District (More than 10,000 students)"
        ])
        focus = st.selectbox("4. What are your primary focus areas for professional growth right now?", list(MULTIMODAL_COSN_CATALOG.keys()))
        time_commit = st.selectbox("5. How much time can you realistically commit to learning each week?", [
            "1 Hour per week (Quick reference tools & checklists)",
            "2-3 Hours per week (Focused webinar series & brief workshops)",
            "4-5 Hours per week (In-depth structured courses & tabletop exercises)",
            "5+ Hours per week (Comprehensive pathways & leadership modules)"
        ])
        
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