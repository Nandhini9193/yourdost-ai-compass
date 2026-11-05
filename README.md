# YourDOST Business Analyst Assignment Submission
## Complete Deliverables Package for the Founder’s Office

**Candidate:** Cheekatipalli Nandhini  
**Role:** Business Analyst, Founder’s Office — YourDOST  
**Evaluator:** Puneet Manuja (Co-Founder, YourDOST) & Founder's Office Team (`associatefo@yourdost.com`)  
**Live Prototype URL:** 🌐 **[https://goat-retired-dee-left.trycloudflare.com](https://goat-retired-dee-left.trycloudflare.com)**  
**Backup Cloud URL:** 🌐 **[https://yourdost-ai-compass.streamlit.app](https://yourdost-ai-compass.streamlit.app)**  
**GitHub Repository:** 📁 **[https://github.com/Nandhini9193/yourdost-ai-compass](https://github.com/Nandhini9193/yourdost-ai-compass)**  

---

### Executive Overview

This repository contains the complete deliverables for the two strategic tasks assigned by YourDOST:
1. **Task 1: Data Analysis & Insights (Gaming Impact)** — In-depth statistical analysis of 100 Indian parents' survey responses, uncovering the School-Age conflict spike ($p = 0.0094$), the counter-intuitive "Rule Paradox", and the protective "Empathy Buffer", packaged into an infographic and supporting analytical report.
2. **Task 2: AI-Powered Product Prototype ("DOST Compass")** — An interactive stepped-care triage navigator that eliminates employee choice paralysis, enforces YourDOST's core platform goal of **Therapist Continuity**, provides zero-latency crisis safety escalation, and delivers real-time clinical ops analytics.

---

### Master Directory of Deliverables

#### 📊 Task 1: Data Analysis & Insights (Parents’ Perceptions of Online Gaming)
| Deliverable | Format | Link | Description |
| :--- | :--- | :--- | :--- |
| **Social-Media Infographic (PNG)** | Image (1260x1900) | [View Infographic Image](./submission/infographic_gaming_impact.png) | High-resolution visual narrative illustrating the 4 core empirical findings and the C.A.R.E. parenting framework. |
| **Social-Media Infographic (PDF)** | Vector PDF | [View Infographic PDF](./submission/infographic_gaming_impact.pdf) | Print-ready, vector PDF version of the infographic. |
| **Infographic Source (HTML)** | Interactive HTML | [View HTML Source](./task1_analysis/infographic_gaming_impact.html) | Standalone responsive HTML/CSS source code with embedded Base64 charts. |
| **Supporting Analysis Document (PDF)** | Executive PDF | [View Task 1 Report (PDF)](./submission/Task1_Data_Analysis_Supporting_Document.pdf) | 2-page concise analysis detailing statistical methodology, hypothesis tests ($t$-tests, Mann-Whitney $U$, ANOVA), behavioral interpretation, and data biases. |
| **Supporting Analysis Document (Markdown)** | Markdown | [View Task 1 Report (Markdown)](./task1_analysis/Task1_Data_Analysis_Supporting_Document.md) | Full source markdown document with complete statistical tables. |
| **Empirical Analysis Code** | Python Scripts | [deep_stats.py](./data/deep_stats.py) & [generate_charts.py](./task1_analysis/generate_charts.py) | Python scripts calculating effect sizes, $p$-values, and rendering high-resolution charts. |

---

#### 🤖 Task 2: Build an AI-Powered Product Prototype ("DOST Compass")
| Deliverable | Format | Link | Description |
| :--- | :--- | :--- | :--- |
| **Live Interactive Prototype (Cloud)** | Web Application | **[Launch DOST Compass](https://goat-retired-dee-left.trycloudflare.com)** | Fully interactive web app with conversational triage, live Box Breathing widget, therapist booking with **Continuity Lock**, and real-time clinical operations metrics. |
| **Prototype Visual Screenshot** | High-Res PNG | [View App Screenshot](./submission/prototype_screenshot.png) | Visual capture of the live running application demonstrating the triage flow and 3-tier care stack. |
| **Product Decisions Document (PDF)** | Executive PDF | [View Task 2 Decisions (PDF)](./submission/Task2_AI_Product_Prototype_Document.pdf) | 2-page document outlining opportunity identification, why AI, assumptions, trade-offs, crisis protocols, and success metrics (Expert Stickiness Rate). |
| **Product Decisions Document (Markdown)** | Markdown | [View Task 2 Decisions (Markdown)](./task2_prototype/Task2_AI_Product_Prototype_Document.md) | Full source markdown document. |
| **Prototype Walkthrough & Demo Guide** | Markdown | [View Walkthrough Guide](./task2_prototype/Task2_Prototype_Walkthrough.md) | Step-by-step walkthrough of 4 end-to-end user journeys (Burnout, Imposter Syndrome, Screen Battle, and Crisis Escalation). |

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
  - 👔 **Priya (Tech Lead):** Workplace Burnout & Sprint Overload $\rightarrow$ Somatic Box Breathing + CBT Counselor Matching with Continuity Lock.
  - 📈 **Rahul (Associate):** Imposter Syndrome & Performance Panic $\rightarrow$ Cognitive Distortion Detangler.
  - 🎮 **Sunita (Parent):** Screen-Time Battles with 8-year-old $\rightarrow$ Collaborative Media Agreement Protocol.
  - ⚠️ **Safety Test:** Critical distress marker detection $\rightarrow$ Immediate suspension of algorithmic bot & takeover by 24/7 YourDOST SOS hotline.
* **Therapist Continuity Lock:** Directly addresses YourDOST's core platform mandate (*"sticking to one expert"*) by permanently pairing the user with one specialist (e.g. Dr. Ananya Sen) so they never have to repeat their backstory.
* **Clinical Operations & HR View:** Real-time dashboard tracking triage volume, severity streams, and an **84.2% Expert Stickiness Rate**.
