# Task 2: Prototype Walkthrough & Demo Guide
## DOST Compass: Interactive AI Stepped-Care Wellbeing Navigator

**Candidate:** Cheekatipalli Nandhini  
**Application:** Business Analyst, Founder’s Office — YourDOST  
**Runnable Demo URL:** `http://localhost:3000` (Local Node.js instance)  
**Visual Reference:** [`prototype_screenshot.png`](file:///C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task2_prototype/prototype_screenshot.png)

---

### 1. Prototype Quickstart Instructions

The prototype is fully implemented, self-contained, and currently active in the workspace environment:
```bash
# Navigate to the prototype directory
cd C:\Users\new\.gemini\antigravity\scratch\yourdost-ba-assignment\task2_prototype

# Start the server (already running in background on port 3000)
node server.js
```
Open any web browser and navigate to: **`http://localhost:3000`**

---

### 2. Guided End-to-End User Journeys

The interface features a **Persona Switcher Bar** across the top, pre-configured with 4 distinct real-world employee profiles to demonstrate end-to-end user journeys with zero typing friction.

```
+──────────────────────────────────────────────────────────────────────────────────────────────────────+
| [⚡ Test User Persona Bar]                                                                           |
| [👔 Priya: Burnout]   [📈 Rahul: Imposter]   [🎮 Sunita: Screen Battle]   [⚠️ Crisis: Safety Alert]   |
+──────────────────────────────────────────────────────────────────────────────────────────────────────+
```

---

#### User Journey 1: Workplace Burnout & Cognitive Overload (Priya — Tech Lead)
1. **User Mindset & Input:**
   - *Persona:* Priya, a senior software engineer feeling crushed by shifting sprint deadlines and micro-management.
   - *Unstructured Input:* `"I've been feeling completely suffocated by sprint deadlines. My manager keeps changing requirements and I can't breathe. I don't know if I'm just burnt out or having a breakdown."`
2. **AI Triage Response (1.4s):**
   - *Clinical Severity:* **Moderate**
   - *Primary Domain:* **Workplace Burnout & Cognitive Overload**
   - *Recommendation Strategy:* **Blended Care** (Immediate physiological down-regulation + 1-on-1 counseling).
3. **The Generated 3-Tier Care Stack:**
   - **Level 1 (Immediate Micro-Relief):** *Somatic Box Breathing (4-4-4-4)* widget appears directly in the viewport. The user clicks *"Start Exercise"* and a visual pulsing circle guides them through 4s Inhale, 4s Hold, 4s Exhale, 4s Hold to stimulate the vagus nerve.
   - **Level 2 (Structured Self-Help Track):** *Reclaiming Workplace Boundaries & Energy Shield* (5 interactive prompts, 8 mins).
   - **Level 3 (Dedicated Expert Match):** Pairs Priya with **Dr. Ananya Sen, Ph.D.** (Senior Clinical Psychologist, 9+ yrs exp, CBT & Burnout specialist).
4. **Continuity Guarantee & Booking:**
   - The UI displays the **Continuity Lock Badge**: *"Permanent Care Partner — Designated for long-term consistency so you never have to re-explain your story."*
   - Priya clicks *"Book Confidential 1-on-1 Session"*, selects a preferred time slot (*Tomorrow at 4:00 PM IST*), and receives an instant booking confirmation: `YD-CONF-XXXXXX`.

---

#### User Journey 2: Imposter Syndrome & Performance Panic (Rahul — Associate)
1. **User Mindset & Input:**
   - *Persona:* Rahul, recently promoted to Senior Associate, terrified of failing his upcoming quarterly review.
   - *Unstructured Input:* `"I just got promoted to Senior Associate and I feel like an absolute fraud. I am paralyzed that in my next review everyone will realize I know nothing and fire me."`
2. **AI Triage Response:**
   - *Clinical Severity:* **Mild–Moderate**
   - *Primary Domain:* **Professional Self-Efficacy & Career Anxiety**
3. **Tailored Care Pathway:**
   - **Level 1 Micro-Relief:** *The Evidence Check: 3-Minute Cognitive Distortion Detangler* (examines catastrophic thinking against objective performance facts).
   - **Level 2 Self-Help:** *Overcoming Imposter Syndrome: The Competence Archetype Guide*.
   - **Level 3 Counselor:** Pairs Rahul with **Rajesh Mukherjee, M.Sc.** (Counseling Psychologist & Workplace Executive Coach).

---

#### User Journey 3: The Parenting Screen-Time Battle (Sunita — Working Mother)
*(Direct Bridge to Task 1 Survey Insights)*
1. **User Mindset & Input:**
   - *Persona:* Sunita, an urban working professional experiencing nightly screaming matches with her 8-year-old child over online gaming (*Free Fire*).
   - *Unstructured Input:* `"Every evening at our house turns into a screaming match over Free Fire and gaming. My 8-year-old throws tantrums when I turn off the tablet. I feel like an awful mother."`
2. **AI Triage Response:**
   - Connects directly to the empirical finding from our survey: **School-age children (6–12) represent the peak domestic conflict cohort ($p = 0.0094$)**.
   - Reassures Sunita with clinical empathy: *"You are not an awful mother. Ages 6–12 are the developmental epicenter of screen battles. Unilateral bans trigger friction; collaborative agreements restore calm."*
3. **Tailored Care Pathway:**
   - **Level 1 Micro-Relief:** *Parental Reset: 2-Minute Pre-Conflict Pause* (guided audio before confronting screen limits).
   - **Level 2 Self-Help:** *From Restrictions to Connection: 7-Day Collaborative Media Agreement* (derived from the YourDOST C.A.R.E. framework).
   - **Level 3 Expert Match:** Pairs Sunita with **Dr. Meera Vasudevan** (Child & Family Psychologist, 12+ yrs exp).

---

#### User Journey 4: The Critical Safety Escalation Protocol (Anonymous User)
1. **User Mindset & Input:**
   - *Expression:* `"I can’t do this anymore. Everything is falling apart and I want to end my life. I don't see any reason to live."`
2. **Zero-Latency Safety Intervention:**
   - The AI algorithm immediately identifies crisis markers (`want to end my life`, `suicide`).
   - Normal chatbot generation is **immediately suspended**. The system never attempts algorithmic counseling on an actively suicidal user.
   - An unmissable, pulsing red **High-Priority Clinical Alert Banner** takes over the screen:
     - Direct 1-click button: *"📞 Connect to On-Call DOST Clinician"*
     - National Emergency Helpline: **Tele-MANAS (14416)**
     - 24/7 Crisis Hotline: **Vandrevala Foundation (+91 9999 666 555)**
   - Simultaneously, an anonymized clinical event is logged to the internal response queue for urgent human follow-up.

---

### 3. Internal Clinical Operations & HR Insights Dashboard

Clicking the **"📊 Clinical & HR Ops View"** button in the top navigation opens a sliding drawer providing real-time visibility for internal teams:
1. **Live Key Metrics:**
   - *Total Triages (24h):* Real-time counter of employee reflections processed.
   - *Expert Stickiness Rate:* **84.2%** (measuring how many users stay with their designated expert vs. switching).
   - *Crisis Escalations:* Real-time count of active emergency interventions triggered.
   - *Avg. Triage Speed:* **1.4 seconds**.
2. **Real-Time Audit Stream:**
   - Displays incoming anonymized triage classifications (Domain, Severity, Continuity Match, Crisis Flags) allowing internal supervisors to audit AI recommendation accuracy in real time.
3. **B2B HR Aggregation:**
   - Demonstrates how data is summarized into high-level organizational wellness themes (e.g. *Sprint Burnout in Engineering*) without ever exposing personal identity or individual messages to corporate management.

---
