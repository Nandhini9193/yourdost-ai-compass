# Task 2: AI-Powered Product Prototype Strategy & Decisions Document
## DOST Compass: AI-Powered Stepped Care Triage & Continuity Navigator

**Author:** Cheekatipalli Nandhini  
**Role Target:** Business Analyst, Founder’s Office — YourDOST  
**Problem Statement:** *How might we use AI to help users identify the most relevant next step in their mental wellbeing journey?*  
**Deliverables Included:**
1. Functional Interactive Prototype: Node.js/Express Runnable Web Application (`http://localhost:3000`)
2. High-Resolution Visual Evidence: `prototype_screenshot.png`
3. Strategic Decisions & Product Architecture Document (This document + PDF export)
4. Comprehensive User Journey Walkthrough Guide (`Task2_Prototype_Walkthrough.md`)

---

### 1. Identifying the Opportunity

#### The Specific User Problem: Choice Paralysis & Emotional Friction at the Front Door
In a B2B employee assistance platform like YourDOST, users arrive under states of acute cognitive overload, burnout, vulnerability, and pervasive stigma. The current industry paradigm confronts these overwhelmed employees with a "catalog of options": 150+ self-help articles, 40+ DIY audio tracks, multiple clinical assessments (PHQ-9, GAD-7), and a directory of dozens of therapists.

This creates severe **cognitive friction and abandonment**:
1. **Choice Paralysis:** When someone is emotionally depleted or experiencing anxiety, deciding whether they need a 45-minute therapy session, a 5-minute breathing exercise, or an article induces decision fatigue.
2. **The "Therapy Chasm":** Jumping directly to booking a 1-on-1 counselor feels intimidating, high-commitment, and socially stigmatized. Conversely, generic articles feel trivializing to someone in deep distress.
3. **The Provider Switching Dilemma (YourDOST Core Challenge):** As highlighted in the prompt, YourDOST operates on a delivery structure where employees can book any expert, but *the business and clinical goal is for them to stick to one expert*. When users don't know who to choose, they bounce across providers, destroying clinical continuity and therapeutic rapport.

#### Why AI is the Right Solution
- **Nuanced Natural Language Interpretation:** Emotional distress is expressed messily (*"I feel like a weight is on my chest and sprint deadlines are crushing me"*), which cannot be mapped by rigid dropdown filters. AI parses sentiment, life domain, and severity without forcing the user to take a clinical test.
- **Dynamic Cognitive Load Reduction (Stepped Care):** Instead of presenting a 50-item catalog, AI synthesizes the user's state into **"The Single Best Next Step"** accompanied by a structured 3-tier care stack.
- **Continuous Safety Monitoring & Zero-Latency Triage:** AI provides immediate, deterministic guardrails to detect crisis/self-harm markers and route to 24/7 human clinicians instantly.

---

### 2. Product Solution & Key Features: "DOST Compass"

```
+---------------------------------------------------------------------------------------------------+
|                                  DOST COMPASS ARCHITECTURE                                        |
+---------------------------------------------------------------------------------------------------+
|  [User Reflection: Unstructured Input]                                                            |
|          │                                                                                        |
|          ▼                                                                                        |
|  [Clinical Triage Engine] ─── (Crisis Signals Detected?) ──► YES ──► [Instant 24/7 Human Hotline] |
|          │                                                                                        |
|          ▼ NO                                                                                     |
|  [Stepped-Care Recommendation Matrix]                                                             |
|   ├── Tier 1 (Immediate Micro-Relief): Somatic Box Breathing / 2-Min Cognitive Reframing          |
|   ├── Tier 2 (Structured Habit Protocol): 7-Day Guided Work-Life Boundary Audio Track             |
|   └── Tier 3 (1-on-1 Counseling with Continuity Lock): Smart Therapist Match (Sticks to 1 Expert) |
|          │                                                                                        |
|          ▼                                                                                        |
|  [Confidential B2B Booking] ──► Locked designated expert for future sessions (0 repeat explanation)|
+---------------------------------------------------------------------------------------------------+
```

#### Core Features
1. **Safe-Space Empathetic Intake:** Natural conversational interface where employees express feelings freely. No clinical jargon or mandatory questionnaires.
2. **Deterministic Safety Guardrails & SOS Escalation:** Real-time regex and contextual pattern matching for crisis keywords (suicide, self-harm, severe despair). Triggers an immediate, unblockable red alert banner with 24/7 YourDOST SOS, national Tele-MANAS (14416), and Vandrevala Foundation helplines.
3. **Stepped-Care Recommendation Engine:**
   - **Level 1 (Immediate Micro-Relief, 2 mins):** Interactive somatic reset embedded directly in the viewport (e.g., visual Box Breathing widget pacing 4-4-4-4 breath cycles).
   - **Level 2 (Self-Guided Structured Program):** Micro-learning modules (e.g., *7-Day Workplace Boundary Shield*).
   - **Level 3 (1-on-1 Expert Match with "Continuity Lock"):** Algorithmically pairs the user with 1 designated psychologist based on clinical domain, corporate context, and language.
4. **The "Continuity Lock" Guarantee:** Explicitly solves YourDOST's operational mandate. Reassures the user: *"Meet Dr. Ananya Sen. She is locked as your dedicated care partner for all future check-ins so you never have to re-explain your backstory."*
5. **Clinical Ops & HR Insights Drawer:** Gives internal clinical response teams real-time visibility into triage volumes and severity streams, while providing corporate HR with anonymized, aggregated burnout indices.

---

### 3. Critical Product Decisions, Assumptions & Trade-Offs

#### Key Assumptions
1. **B2B Trust Ceiling:** Employees will only share vulnerable truths if they are 100% convinced their employer/HR has zero access to individual logs.
2. **Willingness for Low-Stakes Engagement:** A burnt-out employee who declines a 45-minute counseling session will readily engage with a 2-minute somatic breathing exercise, which subsequently lowers the psychological threshold for booking therapy.
3. **Continuity Driver:** Sticking to one counselor produces higher Net Promoter Score (NPS) and clinical symptom improvement (PHQ-4 / GAD-7 delta) than open-market therapist shopping.

#### Strategic Trade-Offs Made
- **Stepped Recommendation vs. Full Catalog Access:**
  - *Decision:* Limit initial view to **one primary recommendation** and a 3-tier care stack, rather than displaying the complete library of 100+ resources.
  - *Trade-Off:* Sacrifice broad content discovery in exchange for slashing cognitive load and decision paralysis.
- **Deterministic Crisis Gating vs. Unconstrained Generative Chat:**
  - *Decision:* In acute distress scenarios, the AI is **hard-coded** to halt open conversational therapy and redirect immediately to human emergency hotlines.
  - *Trade-Off:* The AI never attempts to "counsel" a suicidal or actively self-harming individual. Safety and liability strictly supersede engagement.
- **Rule-Based Hybrid Classifier vs. Pure Black-Box Generative Algorithms:**
  - *Decision:* Utilize structured clinical domain heuristics coupled with sentiment classification rather than an unconstrained generative chatbot.
  - *Trade-Off:* Guarantees predictable, auditable clinical outcomes and eliminates conversational hallucinations.

---

### 4. Handling AI Errors, Privacy & Crisis Escalation

| Risk Area | Failure Mode | Mitigation & System Protocol |
| :--- | :--- | :--- |
| **Crisis & Red Flags** | User expresses self-harm or acute suicidality. | **Zero-Tolerance Human Escalation:** Instant UI takeover. 1-click connection to YourDOST 24/7 on-call supervisor; logs clinical alert; suppresses algorithmic generation. |
| **AI Misclassification** | Mild stress misdiagnosed as severe, or vice-versa. | **Stepped Fallback:** All tiers remain visible on screen. If a user feels counseling is too intensive, they can effortlessly pivot to the Level 1 breathing tool or Level 2 DIY article with zero friction. |
| **B2B Privacy & Stigma** | Employee fears HR retaliation or surveillance. | **Zero Corporate Data Sharing:** Data architecture isolates corporate employer billing IDs from clinical conversation logs. HR dashboards display only $k$-anonymized aggregate indices ($N \ge 50$). |
| **Therapist Misalignment** | User does not feel rapport with matched counselor. | **Frictionless Re-Matching:** While the system defaults to the "Continuity Lock", the user is given a gentle 1-click option: *"Request a different specialist"* without awkwardness. |

---

### 5. Success Metrics & Evaluation Framework

To evaluate whether DOST Compass successfully solves the user problem and aligns with YourDOST’s business objectives, we define a balanced scorecard:

```
+───────────────────────────+───────────────────────────────────────────────────────────────+
| Metric Category           | Specific KPI & Target Benchmark                               |
+───────────────────────────+───────────────────────────────────────────────────────────────+
| 1. Funnel Activation Rate | % of arriving users who complete a "Next Step" within 3 mins  |
|                           | Benchmark: Increase from 22% (baseline) to > 55%              |
+───────────────────────────+───────────────────────────────────────────────────────────────+
| 2. Expert Stickiness Rate | % of counseling clients who book Session 2+ with SAME expert  |
| (YourDOST Core Goal)      | Target: > 75% continuity retention (vs. industry 38%)         |
+───────────────────────────+───────────────────────────────────────────────────────────────+
| 3. Clinical Symptom Delta | Pre-post distress score change (PHQ-4 / Burnout Index)        |
|                           | Target: Statistically significant drop after 3 touchpoints    |
+───────────────────────────+───────────────────────────────────────────────────────────────+
| 4. Safety Audit Accuracy  | Zero missed crisis escalations (100% sensitivity for SOS)     |
|                           | False positive rate < 3%                                      |
+───────────────────────────+───────────────────────────────────────────────────────────────+
```

---
