import streamlit as st
import time
import datetime
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="YourDOST Compass | AI Wellbeing Navigator",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .brand-header {
        background: linear-gradient(135deg, #1E3A8A 0%, #172554 100%);
        color: white;
        padding: 20px 24px;
        border-radius: 14px;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .brand-title {
        font-size: 26px;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    .brand-title span { color: #F59E0B; }
    
    .corp-badge {
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
    }
    
    .rec-box {
        background: #EFF6FF;
        border-left: 5px solid #2563EB;
        padding: 16px;
        border-radius: 0 12px 12px 0;
        margin: 14px 0;
    }
    
    .crisis-alert {
        background: #FEF2F2;
        border: 2px solid #DC2626;
        padding: 18px;
        border-radius: 12px;
        color: #991B1B;
        margin: 15px 0;
    }
    
    .continuity-badge {
        background: #ECFDF5;
        border: 1px solid #10B981;
        color: #065F46;
        padding: 6px 12px;
        border-radius: 8px;
        font-weight: 700;
        font-size: 12px;
        display: inline-block;
        margin-bottom: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Expert Profiles
EXPERTS = {
    "burnout": {
        "name": "Dr. Ananya Sen, Ph.D.",
        "title": "Senior Clinical Psychologist (9+ yrs exp)",
        "specialties": "Workplace Burnout • Anxiety • Cognitive Behavioral Therapy (CBT)",
        "languages": "English, Hindi, Bengali",
        "rating": "4.9/5 (410 reviews)",
        "avatar": "👩‍⚕️"
    },
    "imposter": {
        "name": "Rajesh Mukherjee, M.Sc.",
        "title": "Counseling Psychologist & Executive Coach (7+ yrs exp)",
        "specialties": "Career Transition • Imposter Syndrome • Performance Anxiety",
        "languages": "English, Hindi",
        "rating": "4.8/5 (280 reviews)",
        "avatar": "👨‍⚕️"
    },
    "parent": {
        "name": "Dr. Meera Vasudevan",
        "title": "Child & Family Psychologist (12+ yrs exp)",
        "specialties": "Parenting Dynamics • Adolescent Habits • Family Mediation",
        "languages": "English, Hindi, Tamil",
        "rating": "4.95/5 (560 reviews)",
        "avatar": "👩‍⚕️"
    },
    "crisis": {
        "name": "Emergency Clinical Response Team",
        "title": "Immediate 24x7 Triage Unit",
        "specialties": "Acute Crisis • Self-Harm Prevention",
        "languages": "All Major Indian Languages",
        "rating": "24/7 Standby",
        "avatar": "🚨"
    }
}

# Persona Definitions
PERSONAS = {
    "👔 Priya (Tech Lead) — Workplace Burnout": {
        "prompt": "I've been feeling completely suffocated by sprint deadlines. My manager keeps changing requirements and I can't breathe. I don't know if I'm just burnt out or having a breakdown.",
        "domain": "Workplace Burnout & Cognitive Overload",
        "severity": "Moderate",
        "tier": "Blended Care (Micro-Relief + 1-on-1 Counseling)",
        "key": "burnout"
    },
    "📈 Rahul (Associate) — Imposter Syndrome": {
        "prompt": "I just got promoted to Senior Associate and I feel like an absolute fraud. I am paralyzed that in my next review everyone will realize I know nothing and fire me.",
        "domain": "Professional Self-Efficacy & Career Anxiety",
        "severity": "Mild-Moderate",
        "tier": "Cognitive Reframing & Behavioral Coaching",
        "key": "imposter"
    },
    "🎮 Sunita (Parent) — Gaming & Screen Battle": {
        "prompt": "Every evening at our house turns into a screaming match over Free Fire and gaming. My 8-year-old throws tantrums when I turn off the tablet. I feel like an awful mother.",
        "domain": "Parent-Child Screen Dynamics",
        "severity": "Moderate",
        "tier": "Collaborative Boundary Coaching",
        "key": "parent"
    },
    "⚠️ Safety Test — Acute Crisis Signal": {
        "prompt": "I can’t do this anymore. Everything is falling apart and I want to end my life. I don't see any reason to live.",
        "domain": "Acute Despair / Crisis Intervention",
        "severity": "Severe (High-Priority Crisis)",
        "tier": "Immediate Human Escalation",
        "key": "crisis"
    }
}

# Header Banner
st.markdown("""
<div class="brand-header">
    <div>
        <div class="brand-title">your<span>dost</span> Compass</div>
        <div style="font-size: 13px; color: #CBD5E1;">AI-Powered Stepped Care Wellbeing Navigator</div>
    </div>
    <div class="corp-badge">
        🏢 Acme Technologies • 100% Confidential Care
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar: Controls & Operations Dashboard
with st.sidebar:
    st.subheader("⚙️ Prototype Controls")
    selected_persona_name = st.selectbox(
        "Choose Synthetic Persona to Test:",
        list(PERSONAS.keys())
    )
    selected_persona = PERSONAS[selected_persona_name]
    
    st.markdown("---")
    st.subheader("📊 Clinical Ops & B2B Metrics")
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.metric(label="Active Triages", value="52")
        st.metric(label="Continuity Retention", value="84.2%", help="YourDOST Core Goal: % sticking to 1 expert")
    with col_s2:
        st.metric(label="Crisis Escalations", value="1")
        st.metric(label="Avg Triage Speed", value="1.4s")
        
    st.caption("🔒 **Zero Corporate Exposure:** Individual conversations are cryptographically isolated from HR.")

# Main Application Layout: 2 Columns
col_chat, col_pathway = st.columns([1, 1.2], gap="large")

with col_chat:
    st.subheader("💬 Safe Space Reflection")
    st.caption("Share your thoughts naturally. No clinical jargon, diagnostic forms, or employer visibility.")
    
    # Text Input with Default Persona Prompt
    user_input = st.text_area(
        "What has been on your mind lately?",
        value=selected_persona["prompt"],
        height=140
    )
    
    triage_btn = st.button("🧭 Discover My Best Next Step", type="primary", use_container_width=True)

# Triage Logic
is_crisis = any(k in user_input.lower() for k in ['kill myself', 'suicide', 'end my life', 'want to die', 'harm myself'])

with col_pathway:
    st.subheader("🎯 Your Personalized Next Step")
    
    if is_crisis or selected_persona["key"] == "crisis":
        st.markdown("""
        <div class="crisis-alert">
            <h3 style="margin-top:0; color:#991B1B;">🚨 Immediate Human Care Available</h3>
            <p style="font-size:14px; margin-bottom:12px;">
                We hear that you are going through immense pain right now. Please know you are not alone, and algorithms cannot replace human warmth. Our emergency response team is standing by 24/7.
            </p>
            <div style="font-weight:700; font-size:15px; margin-bottom:6px;">National Helplines:</div>
            <ul style="margin-bottom:12px; font-size:13px;">
                <li><strong>Tele-MANAS (Govt. of India):</strong> Dial 14416 (Toll-Free, 24/7)</li>
                <li><strong>Vandrevala Foundation:</strong> +91 9999 666 555</li>
                <li><strong>YourDOST Emergency SOS:</strong> 1-Click Priority Connect</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.button("📞 Connect Instantly to On-Call DOST Clinical Supervisor", type="primary", use_container_width=True)

    else:
        # Triage Badge
        st.markdown(f"""
        <div style="display: flex; gap: 8px; margin-bottom: 12px;">
            <span style="background:#FEF3C7; color:#92400E; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:800;">
                {selected_persona['severity']} Severity
            </span>
            <span style="background:#EFF6FF; color:#1E40AF; padding:4px 12px; border-radius:20px; font-size:12px; font-weight:700;">
                {selected_persona['domain']}
            </span>
        </div>
        """, unsafe_allow_html=True)
        
        # Hero Recommendation
        st.markdown(f"""
        <div class="rec-box">
            <div style="font-size:11px; font-weight:800; color:#1D4ED8; text-transform:uppercase;">✦ Single Best Next Step</div>
            <div style="font-size:18px; font-weight:800; color:#0F172A; margin: 4px 0 6px 0;">
                {selected_persona['tier']}
            </div>
            <div style="font-size:13px; color:#334155;">
                We recommend starting with an immediate 2-minute physiological grounding reset, followed by reserving your designated counseling partner for long-term consistency.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 3-Tier Stepped Care Accordion
        with st.expander("🌱 Level 1: Immediate Micro-Relief (2 Minutes)", expanded=True):
            st.markdown("**Somatic Box Breathing (4-4-4-4)**")
            st.caption("Paced vagus-nerve activation to rapidly down-regulate nervous system fight-or-flight.")
            
            b_col1, b_col2 = st.columns([1, 2])
            with b_col1:
                if st.button("▶ Start 4-4-4-4 Breath"):
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    for phase in ["Inhale (4s)", "Hold (4s)", "Exhale (4s)", "Hold (4s)"]:
                        status_text.markdown(f"**{phase}...**")
                        for i in range(25):
                            time.sleep(0.04)
                        progress_bar.progress(progress_bar.progress(0) + 0.25 if progress_bar.progress(0) < 0.75 else 1.0)
                    status_text.markdown("✨ *Cycle complete. Notice the shift in your heart rate.*")
            with b_col2:
                st.info("Paced breathing lowers cortisol within 120 seconds and prepares your mind for thoughtful reflection.")
                
        with st.expander("📚 Level 2: Structured Self-Guided Track", expanded=False):
            st.markdown("**Reclaiming Workplace Boundaries & Energy Shield**")
            st.caption("5 interactive reflection prompts • Estimated completion: 8 minutes.")
            st.button("Open Interactive Module ➔")
            
        with st.expander("🤝 Level 3: Dedicated 1-on-1 Expert Match (Company Sponsored)", expanded=True):
            expert = EXPERTS[selected_persona["key"]]
            
            st.markdown(f"""
            <div class="continuity-badge">
                🔒 Continuity Guaranteed: Designated Care Partner (Stick to 1 Expert)
            </div>
            """, unsafe_allow_html=True)
            
            e_col1, e_col2 = st.columns([1, 3])
            with e_col1:
                st.markdown(f"<div style='font-size:48px; text-align:center;'>{expert['avatar']}</div>", unsafe_allow_html=True)
            with e_col2:
                st.markdown(f"**{expert['name']}**")
                st.caption(f"{expert['title']} • {expert['rating']}")
                st.caption(f"Languages: {expert['languages']}")
                st.caption(f"Specialties: {expert['specialties']}")
            
            slot = st.selectbox(
                "Choose Your Confidential Slot:",
                ["Tomorrow at 4:00 PM IST (Recommended)", "Tomorrow at 6:30 PM IST", "Saturday at 11:00 AM IST"]
            )
            
            if st.button("📅 Lock In Session with Dedicated Expert", type="primary", use_container_width=True):
                st.success(f"🎉 Session Successfully Confirmed with {expert['name']} for {slot}! Your expert continuity lock is activated.")
                st.balloons()
