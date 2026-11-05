# YourDOST Business Analyst Assignment Submission
## Complete Deliverables Package for the Founder’s Office

**Candidate:** Cheekatipalli Nandhini  
**Role:** Business Analyst, Founder’s Office — YourDOST  
**Evaluator:** Puneet Manuja (Co-Founder, YourDOST) & Founder's Office Team (`associatefo@yourdost.com`)  
**Live Prototype URL:** 🌐 **[https://yourdost-ai-compass.streamlit.app](https://yourdost-ai-compass.streamlit.app)**  
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
| **Social-Media Infographic (PNG)** | Image (1260x1900) | [View Infographic Image](./infographic_gaming_impact.png) | High-resolution visual narrative illustrating the 4 core empirical findings and the C.A.R.E. parenting framework. |
| **Social-Media Infographic (PDF)** | Vector PDF | [View Infographic PDF](./infographic_gaming_impact.pdf) | Print-ready, vector PDF version of the infographic. |
| **Supporting Analysis Document (PDF)** | Executive PDF | [View Task 1 Report (PDF)](./Task1_Data_Analysis_Supporting_Document.pdf) | 2-page concise analysis detailing statistical methodology, hypothesis tests ($t$-tests, Mann-Whitney $U$, ANOVA), behavioral interpretation, and data biases. |

---

#### 🤖 Task 2: Build an AI-Powered Product Prototype ("DOST Compass")
| Deliverable | Format | Link | Description |
| :--- | :--- | :--- | :--- |
| **Live Interactive Prototype (Cloud)** | Web Application | **[Launch DOST Compass](https://yourdost-ai-compass.streamlit.app)** | Fully interactive web app with conversational triage, live Box Breathing widget, therapist booking with **Continuity Lock**, and real-time clinical operations metrics. |
| **Prototype Visual Screenshot** | High-Res PNG | [View App Screenshot](./prototype_screenshot.png) | Visual capture of the live running application demonstrating the triage flow and 3-tier care stack. |
| **Product Decisions Document (PDF)** | Executive PDF | [View Task 2 Decisions (PDF)](./Task2_AI_Product_Prototype_Document.pdf) | 2-page document outlining opportunity identification, why AI, assumptions, trade-offs, crisis protocols, and success metrics (Expert Stickiness Rate). |

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
