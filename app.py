import streamlit as st
import time

# Force wide mode to properly showcase the split-screen dashboard layout
st.set_page_config(layout="wide", page_title="CoSN PL AI Guide")

# Initialize persistence flags and messaging streams
if "form_submitted" not in st.session_state:
    st.session_state["form_submitted"] = False
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "learning_path_data" not in st.session_state:
    st.session_state["learning_path_data"] = ""
if "selected_focus" not in st.session_state:
    st.session_state["selected_focus"] = ""

# --- Production Data Layer: Production-grade multi-format catalog mapping ---
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

def build_multimodal_path(role, exp, size, focus, time_commit):
    """Processes verified data lookups to construct precise 3-step media learning trajectories."""
    suggestions = MULTIMODAL_COSN_CATALOG.get(focus, [])
    if not suggestions:
        return "### 🗺️ Custom Profile Loaded\nNo specific catalog mapping found."
    
    # Initialize base dashboard layout structure
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
    
    # Dynamically build all 3 distinct suggestion items into the layout
    for item in suggestions:
        md_output += f"""
#### **📍 Phase {item['phase']}**
* **Resource:** [{item['title']}]({item['url']})
* **Time Commitment:** {item['duration']}
* **Strategic Context:** {item['why']}

"""
    
    md_output += f"""
---
### 🚀 Actionable Implementation Guide for {role}:
1. **Pacing Plan:** Use the **{suggestions[0]['duration']}** Foundations course as your long-term roadmap while leveraging the **{suggestions[2]['duration']}** Advanced brief tool for immediate, low-overhead tactical changes.
2. **Cabinet Alignment:** When presenting this **{focus}** pathway to your superintendent, cite the strategic context items provided above to secure baseline professional development funding.
"""
    return md_output

def generate_catalog_response(user_query, current_focus):
    """Scans the new multi-format catalog data to deliver strict internal guidance."""
    query_lower = user_query.lower()
    suggestions = MULTIMODAL_COSN_CATALOG.get(current_focus, [])
    
    if not suggestions:
        return "### 📋 Profile Alignment Reference:\nI am calibrated to only use our curated data catalog to assist you with your active track configuration."

    # Search Logic Option A: Cabinet & Stakeholder Engagement queries
    if any(k in query_lower for k in ["cabinet", "board", "superintendent", "involve", "engage"]):
        return (
            f"### 🏛️ Cabinet Engagement Strategy ({current_focus}):\n\n"
            f"To effectively engage your executive leadership on this track, introduce the intermediate resource: **\"{suggestions[1]['title']}\"**. "
            f"Because it requires an operational timeline of **{suggestions[1]['duration']}**, framing this to your cabinet as an asset protection measure "
            f"rather than an isolated technology initiative ensures optimal stakeholder alignment."
        )
        
    # Search Logic Option B: Time Management & Implementation scheduling