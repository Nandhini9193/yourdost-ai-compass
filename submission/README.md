# YourDOST Business Analyst Assignment Submission
## Strategic Deliverables Package for the Founder’s Office

**Candidate:** Cheekatipalli Nandhini  
**Role:** Business Analyst, Founder’s Office — YourDOST  
**Live Working Prototype (24/7 Cloud):** 🌐 **[https://yourdost-compass-ai.streamlit.app](https://yourdost-compass-ai.streamlit.app)**  
**GitHub Repository:** 📁 **[https://github.com/Nandhini9193/yourdost-ai-compass](https://github.com/Nandhini9193/yourdost-ai-compass)**  

---

### Executive Overview

This repository contains the required deliverables for the two strategic tasks assigned by YourDOST:
1. **Task 1: Data Analysis & Insights (Gaming Impact)** — Empirical statistical analysis of 100 Indian parents' survey responses, uncovering the School-Age domestic conflict spike ($p = 0.0094$), the counter-intuitive "Rule Paradox", and the protective "Empathy Buffer", delivered as an infographic and a 2-page analytical report.
2. **Task 2: AI-Powered Product Prototype ("DOST Compass")** — An interactive stepped-care triage navigator that eliminates employee choice paralysis, enforces YourDOST's core platform mandate of **Therapist Continuity**, provides zero-latency crisis safety escalation, and delivers real-time clinical operations analytics.

---

### Official Required Deliverables

#### 📊 Task 1: Data Analysis & Insights (Parents’ Perceptions of Online Gaming)
| Deliverable (per Prompt) | Format | Access Link | Description |
| :--- | :--- | :--- | :--- |
| **1. One-Page Infographic** | High-Res PNG & Vector PDF | **[View Infographic (PNG)](./infographic_gaming_impact.png)**<br>[Download PDF Version](./infographic_gaming_impact.pdf) | Social-media-ready visual narrative illustrating the 4 core empirical findings and the C.A.R.E. parenting framework. |
| **2. Brief Supporting Document (1–2 Pages)** | Executive PDF | **[View Supporting Document (PDF)](./Task1_Data_Analysis_Supporting_Document.pdf)** | Concise analytical report detailing statistical methodology, hypothesis tests ($t$-tests, Mann-Whitney $U$, ANOVA), behavioral interpretation, and data limitations. |

---

#### 🧭 Task 2: Build an AI-Powered Product Prototype ("DOST Compass")
| Deliverable (per Prompt) | Format | Access Link | Description |
| :--- | :--- | :--- | :--- |
| **1. Working Prototype** | Live 24/7 Cloud App & Runnable Code | **[Launch DOST Compass (Live 24/7 Link)](https://yourdost-compass-ai.streamlit.app)** | Fully interactive web application demonstrating natural conversational intake, live Box Breathing widget, therapist booking with **Continuity Lock**, and real-time clinical ops analytics. |
| **2. Product Decisions Document (Max 2 Pages)** | Executive PDF | **[View Product Decisions (PDF)](./Task2_AI_Product_Prototype_Document.pdf)** | 2-page strategic document outlining opportunity identification, why AI, key assumptions, trade-offs, crisis escalation protocols, and success metrics (Stickiness Rate). |
| **3. Prototype Walkthrough** | Markdown Guide | **[View Prototype Walkthrough Guide](./task2_prototype/Task2_Prototype_Walkthrough.md)** | Step-by-step walkthrough demonstrating 4 end-to-end user journeys (Burnout, Imposter Syndrome, Screen Battle, and Crisis SOS). |

---

### How to Run the Prototype Locally

#### Option A: Run the Streamlit Prototype (Python)
```bash
# 1. Clone the repository
git clone https://github.com/Nandhini9193/yourdost-ai-compass.git
cd yourdost-ai-compass

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

#### Option B: Run the Node.js / Express Prototype
```bash
# 1. Navigate to the Node.js prototype folder
cd task2_prototype

# 2. Install dependencies
npm install

# 3. Launch the server
node server.js
```
Open **`http://localhost:3000`** in your browser.

---

### Core Highlights of the Prototype

* **Persona Switcher:** 1-click testing of realistic employee situations:
  - 👔 **Priya — Workplace Burnout:** Sprint Overload $\rightarrow$ Somatic Box Breathing + CBT Counselor Matching with Continuity Lock.
  - 📈 **Rahul — Imposter Syndrome:** Performance Panic $\rightarrow$ Cognitive Distortion Detangler.
  - 🎮 **Sunita — Screen-Time Battles:** Evening Gaming Friction with 8-year-old $\rightarrow$ Collaborative Media Agreement Protocol.
  - ⚠️ **Crisis SOS:** Critical distress marker detection $\rightarrow$ Immediate suspension of automated chat & takeover by 24/7 YourDOST emergency SOS clinical helpline.
* **Therapist Continuity Lock:** Directly addresses YourDOST's core platform mandate (*"sticking to one expert"*) by permanently pairing the user with one specialist (e.g. Dr. Ananya Sen) so they never have to repeat their backstory.
* **Clinical Operations & HR View:** Real-time dashboard tracking triage volume, severity streams, and an **84.2% Expert Stickiness Rate**.
