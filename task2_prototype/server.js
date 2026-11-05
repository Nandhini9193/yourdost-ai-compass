const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Synthetic expert pool with specialties and continuity locks
const EXPERT_POOL = [
  {
    id: 'exp_01',
    name: 'Dr. Ananya Sen, Ph.D.',
    title: 'Senior Clinical Psychologist',
    experience: '9+ years exp • 3,200+ sessions',
    specialties: ['Workplace Burnout', 'Anxiety & Panic', 'CBT'],
    languages: ['English', 'Hindi', 'Bengali'],
    rating: '4.9/5 (410 reviews)',
    avatar: 'https://images.unsplash.com/photo-1594824813637-bf41655b4fd6?auto=format&fit=crop&w=200&h=200&q=80',
    continuityTag: 'Permanent Care Partner (Recommended for Long-term Continuity)'
  },
  {
    id: 'exp_02',
    name: 'Rajesh Mukherjee, M.Sc.',
    title: 'Counseling Psychologist & Workplace Coach',
    experience: '7+ years exp • 2,400+ sessions',
    specialties: ['Career Transition', 'Imposter Syndrome', 'Executive Stress'],
    languages: ['English', 'Hindi'],
    rating: '4.8/5 (280 reviews)',
    avatar: 'https://images.unsplash.com/photo-1622253692010-333f2da6031d?auto=format&fit=crop&w=200&h=200&q=80',
    continuityTag: 'Permanent Care Partner (Recommended for Long-term Continuity)'
  },
  {
    id: 'exp_03',
    name: 'Dr. Meera Vasudevan',
    title: 'Child & Family Psychologist',
    experience: '12+ years exp • 4,800+ sessions',
    specialties: ['Parenting Dynamics', 'Adolescent Screen Habits', 'Family Counseling'],
    languages: ['English', 'Hindi', 'Tamil'],
    rating: '4.95/5 (560 reviews)',
    avatar: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=200&h=200&q=80',
    continuityTag: 'Permanent Care Partner (Recommended for Long-term Continuity)'
  },
  {
    id: 'exp_04',
    name: 'Crisis Care Team (On-Call)',
    title: 'Immediate 24x7 Emergency Clinical Response',
    experience: 'YourDOST Immediate Triage Unit',
    specialties: ['Acute Panic', 'Self-Harm Risk', 'Emergency De-escalation'],
    languages: ['All Major Indian Languages'],
    rating: '24/7 Available',
    avatar: 'https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=200&h=200&q=80',
    continuityTag: 'Immediate Safety Escalation'
  }
];

// In-memory clinical audit logs and metrics
let triageLogs = [
  { id: 101, timestamp: new Date(Date.now() - 3600000).toISOString(), domain: 'Workplace Burnout', severity: 'Moderate', tier: 'Hybrid (Tool + Counselor)', continuityMatch: 'Dr. Ananya Sen', crisisFlag: false },
  { id: 102, timestamp: new Date(Date.now() - 7200000).toISOString(), domain: 'Imposter Syndrome', severity: 'Mild', tier: 'Self-Help DIY', continuityMatch: 'Rajesh Mukherjee', crisisFlag: false },
  { id: 103, timestamp: new Date(Date.now() - 10800000).toISOString(), domain: 'Parenting Stress', severity: 'Moderate', tier: 'Counselor First', continuityMatch: 'Dr. Meera Vasudevan', crisisFlag: false },
  { id: 104, timestamp: new Date(Date.now() - 14400000).toISOString(), domain: 'Sleep Exhaustion', severity: 'Mild', tier: 'Self-Help DIY', continuityMatch: 'Dr. Ananya Sen', crisisFlag: false }
];

// Crisis keywords
const CRISIS_KEYWORDS = [
  'kill myself', 'suicide', 'end my life', 'want to die', 'harm myself', 
  'cutting myself', 'can’t live anymore', 'no reason to live', 'hang myself'
];

// Intelligent Triage Engine
function analyzeMentalState(text) {
  const t = text.toLowerCase();
  
  // 1. Crisis Check
  const isCrisis = CRISIS_KEYWORDS.some(k => t.includes(k));
  if (isCrisis) {
    return {
      severity: 'Severe (Crisis Flag)',
      domain: 'Acute Crisis / Self-Harm Risk',
      recommendedTier: 'Immediate Human Escalation',
      reasoning: 'Critical distress markers detected requiring instantaneous non-algorithmic human de-escalation and 24/7 safety protocol.',
      primaryNextStep: 'Connect to 24/7 Emergency DOST Counselor Hotline',
      microRelief: {
        title: 'Emergency Grounding & SOS Support',
        duration: 'Instant',
        type: 'sos',
        instruction: 'You are not alone. Please pause, take a slow breath, and connect directly with our emergency clinician on standby.'
      },
      selfHelp: null,
      expert: EXPERT_POOL[3],
      isCrisis: true
    };
  }

  // 2. Parenting / Gaming / Family Conflict
  if (t.includes('game') || t.includes('gaming') || t.includes('kid') || t.includes('child') || t.includes('son') || t.includes('daughter') || t.includes('screen') || t.includes('argue')) {
    return {
      severity: 'Moderate',
      domain: 'Parent-Child Dynamics & Screen Friction',
      recommendedTier: 'Guided Consultation & Boundary Framework',
      reasoning: 'Respondent is experiencing interpersonal strain and parental guilt around rules and screen time. Needs collaborative boundary coaching.',
      primaryNextStep: 'Consultation with Family & Child Psychologist with Continuity Guarantee',
      microRelief: {
        title: 'Parental Reset: 2-Minute Pre-Conflict Pause',
        duration: '2 mins',
        type: 'audio',
        description: 'Guided audio to self-regulate before addressing screen limits with your child.'
      },
      selfHelp: {
        title: 'From Restrictions to Connection: 7-Day Collaborative Media Agreement',
        type: 'Structured Program',
        lessons: '4 Modules • 15 mins total',
        badge: 'Recommended for School-Age Parents'
      },
      expert: EXPERT_POOL[2],
      isCrisis: false
    };
  }

  // 3. Workplace Burnout / Deadlines / Manager
  if (t.includes('work') || t.includes('burnout') || t.includes('exhaust') || t.includes('deadline') || t.includes('manager') || t.includes('boss') || t.includes('suffocat') || t.includes('overwhelm') || t.includes('pressure')) {
    const isHighDistress = t.includes('can’t breathe') || t.includes('panic') || t.includes('break down') || t.includes('crying');
    return {
      severity: isHighDistress ? 'Moderate-High' : 'Moderate',
      domain: 'Workplace Burnout & Cognitive Overload',
      recommendedTier: isHighDistress ? '1-on-1 Dedicated Counseling First' : 'Blended Care (Micro-Relief + Counselor Match)',
      reasoning: 'User exhibits signs of chronic occupational exhaustion, nervous system hyperarousal, and emotional boundary fatigue.',
      primaryNextStep: '2-Minute Box Breathing Reset followed by 1-on-1 Counseling with your Permanent Care Partner',
      microRelief: {
        title: 'Somatic Box Breathing (4-4-4-4)',
        duration: '2 mins',
        type: 'breathing',
        description: 'Vagus nerve stimulation to rapidly lower heart rate and down-regulate sympathetic fight-or-flight.'
      },
      selfHelp: {
        title: 'Reclaiming Workplace Boundaries & Energy Shield',
        type: 'Self-Guided DIY Track',
        lessons: '5 Interactive Prompts • 8 mins',
        badge: 'High Efficacy for Corporate Tech Leads'
      },
      expert: EXPERT_POOL[0],
      isCrisis: false
    };
  }

  // 4. Imposter Syndrome / Career Anxiety / Self-Doubt
  if (t.includes('fail') || t.includes('imposter') || t.includes('not good enough') || t.includes('promot') || t.includes('career') || t.includes('judg') || t.includes('confidence') || t.includes('doubt')) {
    return {
      severity: 'Mild-Moderate',
      domain: 'Professional Self-Efficacy & Career Anxiety',
      recommendedTier: 'Cognitive Reframing & Behavioral Coaching',
      reasoning: 'User displays negative internal self-talk, cognitive distortion (mind reading / catastrophizing), and performance anxiety.',
      primaryNextStep: 'Interactive Cognitive Reframing Tool + Executive Counseling Slot',
      microRelief: {
        title: 'The Evidence Check: 3-Minute Cognitive Distortion Detangler',
        duration: '3 mins',
        type: 'reframing',
        description: 'Examine negative workplace assumptions against objective facts.'
      },
      selfHelp: {
        title: 'Overcoming Imposter Syndrome: The Competence Archetype Guide',
        type: 'Curated Article & Worksheet',
        lessons: 'Read + Reflect • 6 mins',
        badge: 'Staff Favorite'
      },
      expert: EXPERT_POOL[1],
      isCrisis: false
    };
  }

  // 5. Default / Sleep & General Emotional Wear
  return {
    severity: 'Mild',
    domain: 'General Emotional Health & Circadian Reset',
    recommendedTier: 'Self-Guided Hygiene with Counselor On-Demand',
    reasoning: 'User is seeking emotional balance and proactive mental fitness tools.',
    primaryNextStep: 'Evening Sleep Wind-Down Audio + Dedicated Wellbeing Check-in',
    microRelief: {
      title: '4-7-8 Parasympathetic Sleep Induction',
      duration: '3 mins',
      type: 'breathing',
      description: 'Slow breath pacing to prepare mind and body for restorative rest.'
    },
    selfHelp: {
      title: '21-Day Mindful Decompression Routine',
      type: 'Structured Wellbeing Program',
      lessons: 'Daily 5-min exercises',
      badge: 'B2B Core Wellness'
    },
    expert: EXPERT_POOL[0],
    isCrisis: false
  };
}

// API Routes
app.post('/api/triage', (req, res) => {
  const { userMessage, userPersona } = req.body;
  if (!userMessage) {
    return res.status(400).json({ error: 'userMessage is required' });
  }

  const analysis = analyzeMentalState(userMessage);

  // Log triage event
  const newLog = {
    id: triageLogs.length + 101,
    timestamp: new Date().toISOString(),
    domain: analysis.domain,
    severity: analysis.severity,
    tier: analysis.recommendedTier,
    continuityMatch: analysis.expert.name,
    crisisFlag: analysis.isCrisis
  };
  triageLogs.unshift(newLog);

  res.json({
    success: true,
    userMessage,
    userPersona: userPersona || 'Anonymous Corporate Employee',
    triageResult: analysis
  });
});

app.post('/api/book-session', (req, res) => {
  const { expertId, timeSlot, continuityAccepted } = req.body;
  const expert = EXPERT_POOL.find(e => e.id === expertId) || EXPERT_POOL[0];
  
  res.json({
    success: true,
    bookingId: 'YD-CONF-' + Math.floor(100000 + Math.random() * 900000),
    expertName: expert.name,
    timeSlot: timeSlot || 'Tomorrow at 4:00 PM IST',
    continuityStatus: 'LOCKED — Dr. ' + expert.name.split(' ')[1] + ' is now your designated primary expert for all future check-ins.',
    message: 'Your session has been securely confirmed. No corporate HR or management has visibility into this booking.'
  });
});

app.get('/api/admin/metrics', (req, res) => {
  const total = triageLogs.length;
  const crisisCount = triageLogs.filter(l => l.crisisFlag).length;
  const severeCount = triageLogs.filter(l => l.severity.includes('Severe') || l.severity.includes('High')).length;
  const moderateCount = triageLogs.filter(l => l.severity.includes('Moderate')).length;
  const mildCount = triageLogs.filter(l => l.severity.includes('Mild')).length;

  res.json({
    totalTriages: total,
    crisisEscalations: crisisCount,
    severityBreakdown: {
      severeOrCrisis: severeCount,
      moderate: moderateCount,
      mild: mildCount
    },
    continuityRetentionRate: '84.2%', // Synthetic operational benchmark
    averageTimeToTriageSeconds: '1.4s',
    recentLogs: triageLogs.slice(0, 8)
  });
});

app.listen(PORT, () => {
  console.log(`YourDOST AI Prototype ("DOST Compass") running at http://localhost:${PORT}`);
});
