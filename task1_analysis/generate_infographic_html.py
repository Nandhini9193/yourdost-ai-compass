import base64
import os

charts_dir = 'C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task1_analysis/charts'

def get_base64(filename):
    path = os.path.join(charts_dir, filename)
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

b64_c1 = get_base64('chart1_age_pressure_cooker.png')
b64_c2 = get_base64('chart2_cognitive_dissonance.png')
b64_c3 = get_base64('chart3_rule_paradox.png')
b64_c4 = get_base64('chart4_empathy_buffer.png')

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>YourDOST Research: The Indian Gaming Paradox</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Cabinet+Grotesk:wght@700;800;900&display=swap');

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: #0F172A;
    color: #0F172A;
    display: flex;
    justify-content: center;
    padding: 24px;
    -webkit-print-color-adjust: exact;
  }}

  .infographic-canvas {{
    width: 1200px;
    background: #FFFFFF;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.4);
    display: flex;
    flex-direction: column;
  }}

  /* HEADER */
  .header {{
    background: linear-gradient(135deg, #1E3A8A 0%, #1E1B4B 60%, #0F172A 100%);
    color: #FFFFFF;
    padding: 36px 48px;
    position: relative;
    border-bottom: 5px solid #F59E0B;
  }}

  .brand-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255, 255, 255, 0.12);
    border: 1px solid rgba(255, 255, 255, 0.25);
    padding: 6px 14px;
    border-radius: 9999px;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #FBBF24;
    margin-bottom: 14px;
  }}

  .header h1 {{
    font-family: 'Cabinet Grotesk', sans-serif;
    font-size: 38px;
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: -0.02em;
    margin-bottom: 10px;
    color: #FFFFFF;
  }}

  .header h1 span {{
    color: #F59E0B;
  }}

  .header p {{
    font-size: 16px;
    color: #CBD5E1;
    max-width: 900px;
    line-height: 1.5;
  }}

  /* HERO METRICS */
  .hero-strip {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    padding: 24px 48px;
    background: #F8FAFC;
    border-bottom: 1px solid #E2E8F0;
  }}

  .stat-card {{
    background: #FFFFFF;
    padding: 20px 18px;
    border-radius: 14px;
    border: 1px solid #E2E8F0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow: hidden;
  }}

  .stat-card::before {{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 5px;
    height: 100%;
  }}

  .stat-card.red::before {{ background: #EF4444; }}
  .stat-card.blue::before {{ background: #3B82F6; }}
  .stat-card.amber::before {{ background: #F59E0B; }}
  .stat-card.teal::before {{ background: #10B981; }}

  .stat-val {{
    font-family: 'Cabinet Grotesk', sans-serif;
    font-size: 36px;
    font-weight: 900;
    line-height: 1;
    margin-bottom: 6px;
  }}

  .stat-card.red .stat-val {{ color: #DC2626; }}
  .stat-card.blue .stat-val {{ color: #2563EB; }}
  .stat-card.amber .stat-val {{ color: #D97706; }}
  .stat-card.teal .stat-val {{ color: #059669; }}

  .stat-label {{
    font-size: 13px;
    font-weight: 700;
    color: #1E293B;
    margin-bottom: 4px;
  }}

  .stat-sub {{
    font-size: 11px;
    color: #64748B;
    line-height: 1.3;
  }}

  /* MAIN GRID */
  .grid-2x2 {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    padding: 32px 48px;
    background: #FFFFFF;
  }}

  .insight-panel {{
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 16px;
    padding: 20px 22px;
    display: flex;
    flex-direction: column;
  }}

  .panel-header {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 12px;
  }}

  .panel-num {{
    background: #1E3A8A;
    color: #FFFFFF;
    font-weight: 800;
    font-size: 13px;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}

  .panel-title-wrap h3 {{
    font-size: 16px;
    font-weight: 800;
    color: #0F172A;
    line-height: 1.25;
  }}

  .panel-title-wrap span {{
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #2563EB;
  }}

  .chart-img-wrap {{
    background: #FFFFFF;
    border-radius: 10px;
    border: 1px solid #E2E8F0;
    padding: 8px;
    margin-bottom: 12px;
  }}

  .chart-img-wrap img {{
    width: 100%;
    height: auto;
    display: block;
    border-radius: 6px;
  }}

  .panel-takeaway {{
    font-size: 12.5px;
    line-height: 1.45;
    color: #334155;
    background: #FFFFFF;
    border-left: 3px solid #3B82F6;
    padding: 8px 12px;
    border-radius: 0 8px 8px 0;
    margin-top: auto;
  }}

  .panel-takeaway strong {{
    color: #0F172A;
  }}

  /* ACTIONABLE FRAMEWORK */
  .framework-section {{
    background: linear-gradient(135deg, #EFF6FF 0%, #F0FDF4 100%);
    border-top: 1px solid #E2E8F0;
    border-bottom: 1px solid #E2E8F0;
    padding: 28px 48px;
  }}

  .framework-title {{
    text-align: center;
    margin-bottom: 20px;
  }}

  .framework-title h3 {{
    font-family: 'Cabinet Grotesk', sans-serif;
    font-size: 22px;
    font-weight: 900;
    color: #1E3A8A;
    margin-bottom: 4px;
  }}

  .framework-title p {{
    font-size: 13px;
    color: #475569;
  }}

  .care-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
  }}

  .care-box {{
    background: #FFFFFF;
    border-radius: 12px;
    padding: 16px;
    border: 1px solid #CBD5E1;
    box-shadow: 0 2px 4px rgba(0,0,0,0.04);
  }}

  .care-letter {{
    display: inline-block;
    font-family: 'Cabinet Grotesk', sans-serif;
    font-size: 24px;
    font-weight: 900;
    color: #1E3A8A;
    line-height: 1;
    margin-bottom: 6px;
  }}

  .care-heading {{
    font-size: 13px;
    font-weight: 800;
    color: #0F172A;
    margin-bottom: 4px;
  }}

  .care-desc {{
    font-size: 11.5px;
    color: #475569;
    line-height: 1.4;
  }}

  /* FOOTER */
  .footer {{
    background: #0F172A;
    color: #94A3B8;
    padding: 20px 48px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
  }}

  .footer-left {{
    max-width: 750px;
    line-height: 1.4;
  }}

  .footer-left strong {{
    color: #F8FAFC;
  }}

  .footer-right {{
    text-align: right;
  }}

  .footer-badge {{
    background: #1E293B;
    border: 1px solid #334155;
    padding: 6px 12px;
    border-radius: 8px;
    color: #38BDF8;
    font-weight: 700;
    display: inline-block;
  }}
</style>
</head>
<body>

<div class="infographic-canvas">

  <!-- HEADER -->
  <div class="header">
    <div class="brand-badge">⚡ YourDOST Clinical & Behavioral Insights Study</div>
    <h1>The Indian Gaming Paradox: <span>Why Rules Backfire</span> & How Connection Heals the Divide</h1>
    <p>A primary investigation of 100 Indian parents reveals a hidden developmental pressure cooker, the failure of rigid bans, and the transformative power of parental empathy.</p>
  </div>

  <!-- HERO METRIC STRIP -->
  <div class="hero-strip">
    <div class="stat-card red">
      <div class="stat-val">94.0%</div>
      <div class="stat-label">Fear Addiction Risk</div>
      <div class="stat-sub">56.7% report acute "High Fear"; 91% dread academic fallout.</div>
    </div>
    <div class="stat-card blue">
      <div class="stat-val">55.2%</div>
      <div class="stat-label">See It as Stress Relief</div>
      <div class="stat-sub">Parents acknowledge gaming relieves pressure, yet feel helpless.</div>
    </div>
    <div class="stat-card amber">
      <div class="stat-val">2.01<span style="font-size:20px;">/3</span></div>
      <div class="stat-label">Peak Conflict at Ages 6–12</div>
      <div class="stat-sub">Primary schoolers face 40% higher friction than teens (p = 0.009).</div>
    </div>
    <div class="stat-card teal">
      <div class="stat-val">-27.5%</div>
      <div class="stat-label">Strain Dropped by Empathy</div>
      <div class="stat-sub">Parents who "understand why" kids play report far less domestic tension.</div>
    </div>
  </div>

  <!-- 2x2 INSIGHTS GRID -->
  <div class="grid-2x2">

    <!-- PANEL 1 -->
    <div class="insight-panel">
      <div class="panel-header">
        <div class="panel-num">1</div>
        <div class="panel-title-wrap">
          <span>Developmental Epicenter</span>
          <h3>The School-Age Pressure Cooker (Ages 6–12)</h3>
        </div>
      </div>
      <div class="chart-img-wrap">
        <img src="data:image/png;base64,{b64_c1}" alt="School Age Pressure Cooker Chart">
      </div>
      <div class="panel-takeaway">
        <strong>Key Insight:</strong> Domestic friction peaks sharply during ages 6–12 (Impact: <strong>2.01 vs 1.43</strong>, p = 0.0094). As formal schooling begins and self-regulation remains immature, screen battles escalate. By teenage years and adulthood (18+), parents either concede autonomy or exhaust intervention.
      </div>
    </div>

    <!-- PANEL 2 -->
    <div class="insight-panel">
      <div class="panel-header">
        <div class="panel-num">2</div>
        <div class="panel-title-wrap">
          <span>Parental Cognitive Dissonance</span>
          <h3>The Split Mind: Catharsis vs Dread</h3>
        </div>
      </div>
      <div class="chart-img-wrap">
        <img src="data:image/png;base64,{b64_c2}" alt="Cognitive Dissonance Chart">
      </div>
      <div class="panel-takeaway">
        <strong>Key Insight:</strong> <strong>55.2%</strong> of parents recognize gaming as a genuine stress-buster, yet <strong>86.6%</strong> label it a distraction and <strong>94%</strong> live with persistent fear of addiction. Parents are paralyzed between acknowledging emotional coping and dreading psychological dependency.
      </div>
    </div>

    <!-- PANEL 3 -->
    <div class="insight-panel">
      <div class="panel-header">
        <div class="panel-num">3</div>
        <div class="panel-title-wrap">
          <span>Behavioral Anomaly</span>
          <h3>The Rule Paradox: Rigid Bans Breed Conflict</h3>
        </div>
      </div>
      <div class="chart-img-wrap">
        <img src="data:image/png;base64,{b64_c3}" alt="The Rule Paradox Chart">
      </div>
      <div class="panel-takeaway">
        <strong>Key Insight:</strong> Total rule count has virtually zero correlation with reduced conflict (rho = 0.076). Worse, <strong>arbitrary schedule bans</strong> ("no gaming on weekdays", "banned during exams") correlate with <em>higher</em> parent-child strain (<strong>1.80 vs 1.44</strong>). Blunt restrictions provoke covert defiance.
      </div>
    </div>

    <!-- PANEL 4 -->
    <div class="insight-panel">
      <div class="panel-header">
        <div class="panel-num">4</div>
        <div class="panel-title-wrap">
          <span>Evidence-Based Solution</span>
          <h3>The Empathy Buffer: Co-Playing Heals Strain</h3>
        </div>
      </div>
      <div class="chart-img-wrap">
        <img src="data:image/png;base64,{b64_c4}" alt="The Empathy Buffer Chart">
      </div>
      <div class="panel-takeaway">
        <strong>Key Insight:</strong> Parents who take time to understand why kids play report significantly lower anxiety (<strong>3.21 vs 3.57</strong>, p = 0.029) and 27.5% less relationship strain. Co-playing parents who replace surveillance with mutual discovery experience the lowest anxiety (<strong>2.86</strong>).
      </div>
    </div>

  </div>

  <!-- FRAMEWORK SECTION -->
  <div class="framework-section">
    <div class="framework-title">
      <h3>The YourDOST C.A.R.E. Parenting Playbook</h3>
      <p>Moving from Reactive Surveillance to Connected Digital Wellbeing</p>
    </div>
    <div class="care-grid">
      <div class="care-box">
        <div class="care-letter">C</div>
        <div class="care-heading">Connect Before Correcting</div>
        <div class="care-desc">Play 1 round of their favorite game together weekly. Shared understanding dissolves defensiveness.</div>
      </div>
      <div class="care-box">
        <div class="care-letter">A</div>
        <div class="care-heading">Agree on Collaborative Caps</div>
        <div class="care-desc">Ditch arbitrary day-bans. Co-create daily duration limits (e.g. 45-min windows) with clear visual timers.</div>
      </div>
      <div class="care-box">
        <div class="care-letter">R</div>
        <div class="care-heading">Recognize Emotional Drivers</div>
        <div class="care-desc">Ask: <em>"Are they playing for mastery, peer bonding, or stress avoidance?"</em> Address root emotional needs.</div>
      </div>
      <div class="care-box">
        <div class="care-letter">E</div>
        <div class="care-heading">Early Scaffolding (Ages 6-12)</div>
        <div class="care-desc">Focus parental energy on primary schoolers where healthy self-regulation habits are successfully cemented.</div>
      </div>
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer">
    <div class="footer-left">
      <strong>Methodology & Sample Note:</strong> Primary survey conducted by YourDOST (N=100 Indian parents; N=67 active gaming households). 64.2% Female, 35.8% Male respondents across major Indian metros (Kolkata 25%, Bangalore 21%, Delhi, Mumbai). Statistical significance tested via two-tailed t-tests, Mann-Whitney U, and ANOVA at alpha = 0.05.
    </div>
    <div class="footer-right">
      <div class="footer-badge">www.yourdost.com</div>
      <div style="margin-top: 4px; font-size: 10px; color: #64748B;">Emotional Wellness for Families & Workplaces</div>
    </div>
  </div>

</div>

</body>
</html>
"""

html_path = 'C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/task1_analysis/infographic_gaming_impact.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated HTML infographic at: {html_path}")
