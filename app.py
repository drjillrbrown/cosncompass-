import streamlit as st
import time

# Force wide mode instantly before executing any secondary properties
st.set_page_config(layout="wide", page_title="CoSN PL AI Guide")

# --- Production Data Layer: Full 5-Track Multi-Format Catalog Mapping ---
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
            "why": "A panel of active interim superintendents and CTOs sharing real-world compliance successes and legal hurdles under FERPA/COPPA updates."
        }
    ],
    "Strategic Leadership, District Visioning & Stakeholder Communication": [
        {
            "phase": "1. Foundations (Course)",
            "title": "CETL® K-12 CTO's Framework of Essential Skills Foundation Course",
            "url": "https://www.cosn.org/courses-workshops-catalog/",
            "duration": "8 weeks",
            "why": "Provides the foundational competencies required to lead systemic EdTech initiatives across districts."
        },
        {
            "phase": "2. Intermediate (Workshop & Toolkit)",
            "title": "CoSN Member Tools & Assessment Resources Portal",
            "url": "https://www.cosn.org",
            "duration": "Self-Directed Download",
            "why": "Peer-tested administrative frameworks and stakeholder slide-decks to cleanly align your executive team."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "EdTech Leadership Trends: Driving Multi-Department Communication",
            "url": "https://www.cosn.org/edtech-topic/webinar-recording/",
            "duration": "1-hour Briefing",
            "why": "Focuses on strategic marketing and language translations needed to pitch complex infrastructure changes to your local board."
        }
    ],
    "IT Management, Budgeting & Infrastructure": [
        {
            "phase": "1. Foundations (Course)",
            "title": "Unlocking Value of Investment (VOI) and Total Cost of Ownership (TCO) for EdTech Leaders",
            "url": "https://www.cosn.org/courses-workshops-catalog/",
            "duration": "2-week Workshop",
            "why": "Crucial for budgeting and hardware/software lifecycle management within your district infrastructure."
        },
        {
            "phase": "2. Intermediate (Workshop & Toolkit)",
            "title": "CoSN TCO and VOI Pricing Calculators & Implementation Manual",
            "url": "https://www.cosn.org",
            "duration": "Interactive Toolkit",
            "why": "Directly guides you through formal capital planning spreadsheets to calculate accurate device lifecycle costs."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "Smart Budgeting: Preserving Classroom Tech Equity in Tight Fiscal Waves",
            "url": "https://www.cosn.org/edtech-topic/webinar-recording/",
            "duration": "45-minute Panel",
            "why": "Active operational strategies to defend your technical infrastructure investments during local budget contractions."
        }
    ],
    "CETL® Certification Exam Preparation & Foundation Review": [
        {
            "phase": "1. Foundations (Course)",
            "title": "CoSN Certified Education Chief Technology Officer (CETL) Certification Program",
            "url": "https://www.cosn.org/professional-development/cetl-certification/",
            "duration": "Self-Paced or Cohort",
            "why": "The premier national credential demonstrating absolute mastery of the K-12 EdTech leadership matrix."
        },
        {
            "phase": "2. Intermediate (Workshop & Toolkit)",
            "title": "CETL® Examination Content Domain Review & Study Guide",
            "url": "https://www.cosn.org/professional-development/cetl-certification/",
            "duration": "Comprehensive Manual",
            "why": "Provides exact framework breakdowns for the three core leadership domains tested on the exam."
        },
        {
            "phase": "3. Advanced (Webinar & Podcast)",
            "title": "The Road to the CETL: Tips and Strategies from Newly Certified Leaders",
            "url": "https://www.cosn.org/edtech-topic/webinar-recording/",
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
    
    # Header block built using standard string properties
    md_output = "### 🗺️ Your Customized CoSN Multi-Format Learning Path\n\n"
    md_output += f"* **Role/Context:** {role}\n"
    md_output += f"* **Experience Level:** {exp}\n"
    md_output += f"* **District Footprint:** {size}\n"
    md_output += f"* **Realistic Commitment:** {time_commit}\n"
    md_output += f"* **Primary Track Target:** {focus}\n\n"
    md_output += "---\n### 🎓 Your 3-Step Media Ecosystem Roadmap\n\n"
    
    # Looping rows cleanly line-by-line to avoid multiline literal breaks
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
        resp += f"Framing this to your cabinet as an asset protection and strategic continuity measure rather than an isolated technical task ensures baseline alignment."
        return resp
        
    fallback = f"### 📋 Catalog Cross-Reference:\n\n"
    fallback += f"Regarding your query on '{user_query}', your active **{current_focus}** track provides structural support via three distinct formats:\n"
    fallback += f"* **Course:** {suggestions[0]['title']} ({suggestions[0]['duration']})\n"
    fallback += f"* **Workshop:** {suggestions[1]['title']} ({suggestions[1]['duration']})\n"
    fallback += f"* **Webinar/Audio:** {suggestions[2]['title']} ({suggestions[2]['duration']})\n\n"
    fallback += "Review these active hyperlinks in your right dashboard layout panel to select the right medium for your goals."
    return fallback

# Interface Presentation Layer
if not st.session_state["form_submitted"]:
    st.title("🎯 Welcome to the CoSN PL AI Guide")
    st.subheader("Please complete your professional baseline profile to customize your roadmap:")
    with st.form("intake_form"):
        role = st.selectbox