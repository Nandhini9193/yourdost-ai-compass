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
    <div style="display:flex; align-items:center;">
        <img src="data:image/png;base64,{LOGO_B64}" style="height:48px; width:auto;" alt="YourDOST Official Logo">
    </div>
    <div class="yd-nav-links">
        <span class="yd-nav-item">Experts</span>
        <span class="yd-nav-item">Self-Help Library</span>
        <span class="yd-nav-item">Assessments</span>
        <span class="yd-nav-item active">✨ DOST Compass (AI Navigator)</span>
    </div>
    <div style="background:#ECFDF5; border:1px solid #A7F3D0; color:#065F46; padding:6px 14px; border-radius:20px; font-size:12px; font-weight:700;">
        🔒 100% Anonymous & Confidential Care
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
