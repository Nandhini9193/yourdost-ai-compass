import streamlit as st
import time
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="YourDOST Compass | AI Emotional Wellness Navigator",
    page_icon="🧡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# YourDOST Official Brand Design System & CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;500;600;700&family=Poppins:wght@500;600;700;800&display=swap');
    
    :root {
        --yd-purple: #2F2663;
        --yd-purple-light: #513D87;
        --yd-purple-subtle: #F5F3FB;
        --yd-orange: #F47920;
        --yd-orange-hover: #E0650D;
        --yd-orange-subtle: #FFF7ED;
        --yd-text-dark: #212529;
        --yd-text-body: #4A4A4A;
        --yd-text-muted: #717171;
        --yd-border: #E8E6F0;
        --yd-white: #FFFFFF;
    }
    
    html, body, [class*="css"] {
        font-family: 'Open Sans', sans-serif !important;
        color: var(--yd-text-body);
        background-color: #FAF9FC;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        color: var(--yd-purple) !important;
    }
    
    /* YOURDOST OFFICIAL TOP NAVIGATION BAR */
    .yd-navbar {
        background: #FFFFFF;
        padding: 14px 28px;
        border-radius: 12px;
        box-shadow: 0 2px 12px rgba(47, 38, 99, 0.06);
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 2px solid var(--yd-border);
        margin-bottom: 22px;
    }
    
    .yd-logo {
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        font-size: 26px;
        color: var(--yd-purple);
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    
    .yd-logo span {
        color: var(--yd-orange);
    }
    
    .yd-nav-links {
        display: flex;
        gap: 20px;
        align-items: center;
        font-size: 13px;
        font-weight: 600;
        color: #595959;
    }
    
    .yd-nav-item {
        color: #595959;
        text-decoration: none;
        padding: 6px 10px;
        border-radius: 6px;
        transition: all 0.2s;
    }
    
    .yd-nav-item.active {
        color: var(--yd-purple);
        background: var(--yd-purple-subtle);
        font-weight: 700;
    }
    
    .yd-b2b-badge {
        background: #F5F3FB;
        border: 1px solid #D5CEE8;
        color: var(--yd-purple);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    
    /* HERO AI BANNER */
    .yd-hero-banner {
        background: linear-gradient(135deg, #2F2663 0%, #46397E 100%);
        color: #FFFFFF;
        padding: 24px 28px;
        border-radius: 14px;
        margin-bottom: 22px;
        box-shadow: 0 4px 20px rgba(47, 38, 99, 0.15);
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .yd-hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 24px;
        font-weight: 700;
        color: #FFFFFF !important;
        margin-bottom: 4px;
    }
    
    .yd-hero-sub {
        font-size: 13.5px;
        color: #E2DEED;
        max-width: 650px;
        line-height: 1.45;
    }
    
    .yd-feature-pill {
        background: rgba(244, 121, 32, 0.25);
        border: 1px solid #F47920;
        color: #FFB070;
        font-size: 11px;
        font-weight: 700;
        padding: 4px 10px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: inline-block;
        margin-bottom: 8px;
    }
    
    /* CARDS & PANELS */
    .yd-card {
        background: #FFFFFF;
        border: 1px solid var(--yd-border);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(47, 38, 99, 0.04);
        margin-bottom: 16px;
    }
    
    .yd-rec-hero {
        background: var(--yd-orange-subtle);
        border-left: 5px solid var(--yd-orange);
        border-radius: 0 12px 12px 0;
        padding: 16px 20px;
        margin-bottom: 18px;
    }
    
    .yd-rec-badge {
        font-size: 11px;
        font-weight: 800;
        color: var(--yd-orange);
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 4px;
    }
    
    .yd-rec-title {
        font-family: 'Poppins', sans-serif;
        font-size: 17px;
        font-weight: 700;
        color: var(--yd-purple) !important;
        margin-bottom: 6px;
    }
    
    /* BUTTONS */
    .stButton>button {
        background-color: var(--yd-orange) !important;
        color: #FFFFFF !important;
        font-family: 'Poppins', sans-serif !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 20px !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        background-color: var(--yd-orange-hover) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(244, 121, 32, 0.3) !important;
    }
    
    /* CRISIS BANNER */
    .yd-crisis-box {
        background: #FEF2F2;
        border: 2px solid #DC2626;
        border-radius: 12px;
        padding: 18px 22px;
        color: #991B1B;
        margin-bottom: 20px;
    }
    
    /* CONTINUITY BADGE */
    .yd-continuity-tag {
        background: #F5F3FB;
        border: 1px solid #D5CEE8;
        color: var(--yd-purple);
        padding: 6px 12px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 12px;
        display: inline-block;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Synthetic Expert Pool (aligned with YourDOST's verified psychologists)
EXPERTS = {
    "burnout": {
        "name": "Dr. Ananya Sen, Ph.D.",
        "title": "Senior Clinical Psychologist • 9+ yrs exp",
        "specialties": "Workplace Burnout • CBT • Panic & Anxiety",
        "languages": "English, Hindi, Bengali",
        "rating": "4.92/5 (410 reviews)",
        "sessions": "3,400+ corporate sessions",
        "avatar": "👩‍⚕️"
    },
    "imposter": {
        "name": "Rajesh Mukherjee, M.Sc.",
        "title": "Executive Wellbeing & Leadership Coach • 7+ yrs exp",
        "specialties": "Career Transition • Imposter Syndrome • Self-Doubt",
        "languages": "English, Hindi",
        "rating": "4.88/5 (290 reviews)",
        "sessions": "2,200+ corporate sessions",
        "avatar": "👨‍⚕️"
    },
    "parent": {
        "name": "Dr. Meera Vasudevan",
        "title": "Child & Family Psychologist • 12+ yrs exp",
        "specialties": "Parenting Dynamics • Adolescent Digital Habits • Mediation",
        "languages": "English, Hindi, Tamil",
        "rating": "4.95/5 (560 reviews)",
        "sessions": "4,800+ sessions",
        "avatar": "👩‍⚕️"
    },
    "crisis": {
        "name": "YourDOST Emergency Clinical Unit",
        "title": "24x7 Immediate Critical Response Care",
        "specialties": "Acute Crisis • De-escalation • Emergency Triage",
        "languages": "All Major Indian Languages",
        "rating": "Immediate 24/7 Standby",
        "sessions": "24/7 Available",
        "avatar": "🚨"
    }
}

# Synthetic Test Personas
PERSONAS = {
    "👔 Priya (Tech Lead) — Workplace Burnout": {
        "prompt": "I've been feeling completely suffocated by sprint deadlines. My manager keeps changing requirements and I can't breathe. I don't know if I'm just burnt out or having a breakdown.",
        "domain": "Workplace Burnout & Sprint Fatigue",
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
        "domain": "Parent-Child Screen Dynamics (Ages 6-12)",
        "severity": "Moderate",
        "tier": "Collaborative Boundary Coaching",
        "key": "parent"
    },
    "⚠️ Safety Guardrail Test — Acute Crisis Signal": {
        "prompt": "I can’t do this anymore. Everything is falling apart and I want to end my life. I don't see any reason to live.",
        "domain": "Critical Distress / Crisis Triage",
        "severity": "Severe (High-Priority Crisis)",
        "tier": "Immediate Human Escalation",
        "key": "crisis"
    }
}

# TOP NAVIGATION BAR (Mirrors official YourDOST header)
LOGO_B64 = "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"
st.markdown(f"""
<div class="yd-navbar">
    <div style="display:flex; align-items:center; line-height:1;">
        <img src="data:image/png;base64,{LOGO_B64}" style="height:42px; width:auto; display:block; vertical-align:middle; filter:drop-shadow(0 1px 2px rgba(0,0,0,0.05));" alt="YourDOST Official Logo">
    </div>
    <div class="yd-nav-links">
        <span class="yd-nav-item">Experts</span>
        <span class="yd-nav-item">Self-Help Library</span>
        <span class="yd-nav-item">Assessments</span>
        <span class="yd-nav-item active">✨ DOST Compass (AI Navigator)</span>
    </div>
    <div style="background:#ECFDF5; border:1px solid #A7F3D0; color:#065F46; padding:8px 16px; border-radius:20px; font-size:12px; font-weight:700; display:flex; align-items:center; gap:6px; line-height:1;">
        <span>🔒</span> 100% Anonymous & Confidential Care
    </div>
</div>
""", unsafe_allow_html=True)

# HERO AI FEATURE BANNER
st.markdown("""
<div class="yd-hero-banner">
    <div>
        <div class="yd-feature-pill">✦ Built for YourDOST Employee Wellness</div>
        <div class="yd-hero-title">Feeling Overwhelmed? Let DOST Compass Guide You.</div>
        <div class="yd-hero-sub">
            Skip the endless catalog of articles and therapists. Share how you feel in your own words, and receive the single best next step for your emotional health.
        </div>
    </div>
    <div style="text-align: right; font-size: 12px; color: #E2DEED;">
        🔒 <strong>100% Private</strong><br>Your employer never sees your entries.
    </div>
</div>
""", unsafe_allow_html=True)

# SIDEBAR CONTROLS
with st.sidebar:
    st.markdown("<h3 style='color:#2F2663;'>⚙️ Test User Personas</h3>", unsafe_allow_html=True)
    st.caption("Select a real-world scenario to simulate instant triage:")
    
    selected_name = st.selectbox(
        "Choose Persona:",
        list(PERSONAS.keys())
    )
    persona = PERSONAS[selected_name]
    
    st.markdown("---")
    st.markdown("<h3 style='color:#2F2663;'>📊 Clinical Operations View</h3>", unsafe_allow_html=True)
    st.caption("Live metrics for internal YourDOST care supervisors:")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric("Triages Today", "68")
        st.metric("Expert Stickiness", "84.2%", help="YourDOST Core Goal: % sticking to 1 expert")
    with col_m2:
        st.metric("Crisis Alerts", "1")
        st.metric("Triage Latency", "1.3s")
        
    st.info("🔒 **B2B Privacy Guarantee:** All user sessions are cryptographically isolated from corporate HR dashboards.")

# TWO-COLUMN MAIN APPLICATION
col_chat, col_rec = st.columns([1, 1.25], gap="large")

with col_chat:
    st.markdown("<h3 style='color:#2F2663;'>💬 Safe Space Reflection</h3>", unsafe_allow_html=True)
    st.caption("Express what's on your mind. No clinical jargon, diagnostic forms, or ratings.")
    
    user_text = st.text_area(
        "How are you truly feeling right now?",
        value=persona["prompt"],
        height=140
    )
    
    triage_clicked = st.button("🧭 Find My Best Next Step", use_container_width=True)

# Check Crisis Guardrail
crisis_words = ['kill myself', 'suicide', 'end my life', 'want to die', 'harm myself']
is_crisis = any(w in user_text.lower() for w in crisis_words)

with col_rec:
    st.markdown("<h3 style='color:#2F2663;'>🎯 Your Recommended Care Pathway</h3>", unsafe_allow_html=True)
    
    if is_crisis or persona["key"] == "crisis":
        st.markdown("""
        <div class="yd-crisis-box">
            <h3 style="margin-top:0; color:#991B1B !important;">🚨 Immediate Clinical Care on Standby</h3>
            <p style="font-size:13.5px; line-height:1.5; color:#7F1D1D; margin-bottom:12px;">
                We hear that you are carrying deep pain right now. Algorithms cannot replace human empathy. Our 24/7 licensed emergency clinical unit is ready to support you right now.
            </p>
            <div style="font-weight:700; font-size:14px; margin-bottom:6px; color:#991B1B;">Emergency Support Helplines:</div>
            <ul style="font-size:13px; color:#7F1D1D; margin-bottom:14px;">
                <li><strong>YourDOST Priority Emergency Line:</strong> 1-Click Priority Connect</li>
                <li><strong>National Tele-MANAS (Govt. of India):</strong> Dial 14416 (24/7, Toll-Free)</li>
                <li><strong>Vandrevala Foundation Helpline:</strong> +91 9999 666 555</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        st.button("📞 Connect with On-Call DOST Clinical Supervisor", use_container_width=True)
        
    else:
        # Severity & Domain Tags
        st.markdown(f"""
        <div style="display:flex; gap:10px; margin-bottom:14px; align-items:center;">
            <span style="background:#FFF7ED; color:#C2410C; border:1px solid #FFEDD5; padding:4px 12px; border-radius:20px; font-size:11.5px; font-weight:800; text-transform:uppercase;">
                {persona['severity']}
            </span>
            <span style="background:#F5F3FB; color:#2F2663; border:1px solid #D5CEE8; padding:4px 14px; border-radius:20px; font-size:12px; font-weight:700;">
                {persona['domain']}
            </span>
        </div>
        """, unsafe_allow_html=True)
        
        # Single Best Next Step Hero
        st.markdown(f"""
        <div class="yd-rec-hero">
            <div class="yd-rec-badge">✦ Single Best Next Step</div>
            <div class="yd-rec-title">{persona['tier']}</div>
            <div style="font-size:13px; color:#4A4A4A; line-height:1.45;">
                Based on your emotional cues, we recommend immediate physiological down-regulation followed by booking your dedicated long-term care partner.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Stepped Care Stack
        with st.expander("🌱 Step 1: Immediate Micro-Relief (2 Minutes)", expanded=True):
            st.markdown("<strong style='color:#2F2663;'>Somatic Box Breathing (4-4-4-4)</strong>", unsafe_allow_html=True)
            st.caption("Paced vagus-nerve activation to rapidly calm sympathetic nervous system fight-or-flight.")
            
            b_c1, b_c2 = st.columns([1, 2])
            with b_c1:
                if st.button("▶ Start 4-4-4-4 Breath"):
                    prog = st.progress(0.0)
                    stat = st.empty()
                    phases = ["Inhale (4s)", "Hold (4s)", "Exhale (4s)", "Hold (4s)"]
                    for idx, phase in enumerate(phases):
                        stat.markdown(f"**{phase}...**")
                        for _ in range(25):
                            time.sleep(0.04)
                        prog.progress(float((idx + 1) / len(phases)))
                    stat.markdown("✨ *Cycle complete. Feel your heart rate settling.*")
            with b_c2:
                st.caption("💡 120 seconds of paced respiration significantly reduces salivary cortisol and cognitive overwhelm.")
                
        with st.expander("📚 Step 2: Self-Guided Habit Track", expanded=False):
            st.markdown("<strong style='color:#2F2663;'>Reclaiming Workplace Boundaries & Energy Shield</strong>", unsafe_allow_html=True)
            st.caption("5 interactive micro-prompts designed for high-stress corporate environments • 8 mins.")
            st.button("Open Self-Guided Module ➔")
            
        with st.expander("🤝 Step 3: Dedicated Expert Match (Company Sponsored)", expanded=True):
            expert = EXPERTS[persona["key"]]
            
            st.markdown("""
            <div class="yd-continuity-tag">
                🔒 <strong>Continuity Lock:</strong> Sticking to 1 Expert for Long-Term Trust
            </div>
            """, unsafe_allow_html=True)
            
            exp_c1, exp_c2 = st.columns([1, 3.5])
            with exp_c1:
                st.markdown(f"<div style='font-size:52px; text-align:center;'>{expert['avatar']}</div>", unsafe_allow_html=True)
            with exp_c2:
                st.markdown(f"<strong style='font-size:16px; color:#2F2663;'>{expert['name']}</strong>", unsafe_allow_html=True)
                st.caption(f"{expert['title']} • {expert['rating']}")
                st.caption(f"Specialties: {expert['specialties']}")
                st.caption(f"Languages: {expert['languages']} • {expert['sessions']}")
            
            slot = st.selectbox(
                "Choose Your Confidential Slot:",
                ["Tomorrow at 4:00 PM IST (Recommended)", "Tomorrow at 6:30 PM IST", "Saturday at 11:00 AM IST"]
            )
            
            if st.button(f"📅 Book Confidential Session with {expert['name'].split(',')[0]}", use_container_width=True):
                st.success(f"🎉 Session Confirmed with {expert['name']} for {slot}! Your expert continuity lock is activated.")
                st.balloons()
