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
st.markdown("""
<div class="yd-navbar">
    <div class="yd-logo">
        your<span>dost</span>
    </div>
    <div class="yd-nav-links">
        <span class="yd-nav-item">Experts</span>
        <span class="yd-nav-item">Self-Help Library</span>
        <span class="yd-nav-item">Assessments</span>
        <span class="yd-nav-item active">✨ DOST Compass (AI Navigator)</span>
    </div>
    <div class="yd-b2b-badge">
        🏢 Acme Technologies • Confidential EAP
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
                    prog = st.progress(0)
                    stat = st.empty()
                    for phase in ["Inhale (4s)", "Hold (4s)", "Exhale (4s)", "Hold (4s)"]:
                        stat.markdown(f"**{phase}...**")
                        for _ in range(25):
                            time.sleep(0.04)
                        prog.progress(min(1.0, prog.progress(0) + 0.25))
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
