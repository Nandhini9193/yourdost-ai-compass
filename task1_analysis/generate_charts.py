import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

base_dir = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(base_dir, 'charts')
os.makedirs(out_dir, exist_ok=True)

data_path = os.path.join(base_dir, '..', 'data', 'cleaned_active_survey.csv')
df = pd.read_csv(data_path)

def is_shooter(text):
    if pd.isna(text):
        return 0
    t = str(text).lower()
    shooter_keywords = ['pubg', 'pubgee', 'free fire', 'freefire', 'call of duty', 'counter strike', 'brawhalla', 'mortal kombat']
    return 1 if any(k in t for k in shooter_keywords) else 0

df['has_shooter'] = df['games_named'].apply(is_shooter)


# Colors
C_PRIMARY = '#1E3A8A'   # Deep Blue
C_ACCENT = '#3B82F6'    # Bright Blue
C_CORAL = '#EF4444'     # Red/Coral for fear/conflict
C_TEAL = '#10B981'      # Teal/Green for positive
C_AMBER = '#F59E0B'     # Amber
C_PURPLE = '#8B5CF6'    # Purple
C_GRAY = '#64748B'      # Slate Gray

# -------------------------------------------------------------
# Chart 1: The School-Age Pressure Cooker (Ages 6-12)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
age_metrics = df.groupby('kid_age_group')[['impact_frustration_num', 'impact_conflict_num', 'impact_strain_num', 'overall_impact_score']].mean()
# Filter out infants (n=1) for clean visual comparison
age_metrics_filtered = age_metrics.loc[['Pre-school (4-5 years old)', 'School Age (6-12 years old)', 'Adolescents (13-17 years old)', 'Adults (18 years and above)']]
labels = ['Pre-school\n(4-5 yrs, n=8)', 'School Age\n(6-12 yrs, n=25)', 'Adolescents\n(13-17 yrs, n=10)', 'Adults\n(18+ yrs, n=23)']

x = np.arange(len(labels))
width = 0.22

rects1 = ax.bar(x - width, age_metrics_filtered['impact_frustration_num'], width, label='Family Frustrations', color='#F87171')
rects2 = ax.bar(x, age_metrics_filtered['impact_conflict_num'], width, label='Arguments / Conflicts', color='#FB923C')
rects3 = ax.bar(x + width, age_metrics_filtered['impact_strain_num'], width, label='Parent-Child Strain', color='#FBBF24')

ax.set_ylabel('Impact Level (0 = None, 3 = High)', fontsize=11, fontweight='bold', color='#1E293B')
ax.set_title('The School-Age Pressure Cooker: Family Friction Spikes at Ages 6–12 (p = 0.0094)', fontsize=12, fontweight='bold', pad=15, color='#0F172A')
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=10, color='#334155')
ax.set_ylim(0, 3.0)
ax.axhline(y=1.5, color='#CBD5E1', linestyle='--', linewidth=1)
ax.legend(frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=9)

# Highlight School Age
for bar in [rects1[1], rects2[1], rects3[1]]:
    bar.set_edgecolor('#B91C1C')
    bar.set_linewidth(1.8)

# Add values on top of bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold', color='#1E293B')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)

plt.tight_layout()
plt.savefig(f'{out_dir}/chart1_age_pressure_cooker.png')
plt.close()

# -------------------------------------------------------------
# Chart 2: The Cognitive Dissonance (Fears vs Benefits)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5), dpi=300)
categories = [
    'Addiction Risk',
    'Academic Disruption',
    'Inappropriate Content',
    'Health Issues',
    'Violent Behavior',
    'View: Good Stress-Buster',
    'View: Beneficial to Kids',
    'View: Socialization Tool'
]
percentages = [
    (df['fear_addiction_num'] >= 3).mean() * 100,
    (df['fear_academics_num'] >= 3).mean() * 100,
    (df['fear_content_num'] >= 3).mean() * 100,
    (df['fear_health_num'] >= 3).mean() * 100,
    (df['fear_violence_num'] >= 3).mean() * 100,
    (df['perc_stress_buster_num'] >= 4).mean() * 100,
    (df['perc_beneficial_num'] >= 4).mean() * 100,
    (df['perc_socialize_num'] >= 4).mean() * 100
]
colors = [C_CORAL, C_CORAL, '#F87171', '#F87171', '#FB923C', C_TEAL, C_TEAL, C_TEAL]

y_pos = np.arange(len(categories))
bars = ax.barh(y_pos, percentages, color=colors, height=0.65, edgecolor='#334155', linewidth=0.5)

ax.set_yticks(y_pos)
ax.set_yticklabels(categories, fontsize=10, fontweight='bold', color='#1E293B')
ax.invert_yaxis()  # top-down
ax.set_xlabel('Percentage of Parents (%)', fontsize=11, fontweight='bold', color='#1E293B')
ax.set_title('The Parental Dilemma: Severe Fears vs Recognized Emotional Catharsis', fontsize=12, fontweight='bold', pad=15, color='#0F172A')
ax.set_xlim(0, 105)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 1.5, bar.get_y() + bar.get_height()/2, f'{width:.1f}%', 
            va='center', ha='left', fontsize=9, fontweight='bold', color='#1E293B')

# Annotation dividing lines
ax.axhline(y=4.5, color='#94A3B8', linestyle=':', linewidth=1.5)
ax.text(55, 4.3, '▼ Acute Parental Fears (Med–High)', fontsize=8.5, color='#B91C1C', fontweight='bold')
ax.text(55, 4.8, '▲ Perceived Value & Benefits (Agree)', fontsize=8.5, color='#047857', fontweight='bold')

plt.tight_layout()
plt.savefig(f'{out_dir}/chart2_cognitive_dissonance.png')
plt.close()

# -------------------------------------------------------------
# Chart 3: The Rule Paradox (Rules vs Conflict)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=300)
rule_labels = [
    'Days of Week\nBan',
    'No Games\nDuring Exams',
    'Specific Kinds\nOnly',
    'Fixed Duration\nLimit',
    'Times of Day\nLimit',
    'No Rules\nWhatsoever'
]

impact_with_rule = [
    df[df['rule_days_of_week_num'] == 1]['overall_impact_score'].mean(),
    df[df['rule_no_exams_num'] == 1]['overall_impact_score'].mean(),
    df[df['rule_certain_kinds_num'] == 1]['overall_impact_score'].mean(),
    df[df['rule_fixed_duration_num'] == 1]['overall_impact_score'].mean(),
    df[df['rule_times_of_day_num'] == 1]['overall_impact_score'].mean(),
    df[df['rule_no_rules_num'] == 1]['overall_impact_score'].mean()
]

impact_without_rule = [
    df[df['rule_days_of_week_num'] == 0]['overall_impact_score'].mean(),
    df[df['rule_no_exams_num'] == 0]['overall_impact_score'].mean(),
    df[df['rule_certain_kinds_num'] == 0]['overall_impact_score'].mean(),
    df[df['rule_fixed_duration_num'] == 0]['overall_impact_score'].mean(),
    df[df['rule_times_of_day_num'] == 0]['overall_impact_score'].mean(),
    df[df['rule_no_rules_num'] == 0]['overall_impact_score'].mean()
]

x = np.arange(len(rule_labels))
w = 0.35

r1 = ax.bar(x - w/2, impact_with_rule, w, label='With Rule Enforced', color='#DC2626')
r2 = ax.bar(x + w/2, impact_without_rule, w, label='Without This Rule', color='#38BDF8')

ax.set_ylabel('Family Impact Score (0-3)', fontsize=11, fontweight='bold', color='#1E293B')
ax.set_title('The Rule Paradox: Rigid Schedule Bans Correlate with HIGHER Family Friction', fontsize=12, fontweight='bold', pad=15, color='#0F172A')
ax.set_xticks(x)
ax.set_xticklabels(rule_labels, fontsize=9.5, color='#334155')
ax.set_ylim(0, 2.5)
ax.legend(frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=9)

for rect in r1 + r2:
    h = rect.get_height()
    ax.annotate(f'{h:.2f}', xy=(rect.get_x() + rect.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{out_dir}/chart3_rule_paradox.png')
plt.close()

# -------------------------------------------------------------
# Chart 4: The Empathy & Co-Playing Dividend
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.2), dpi=300)
dimensions = [
    'I Understand Why\nKids Play',
    'I Have Played Games\nMyself',
    'I Play Games\nWith My Kids'
]

fear_yes = [
    df[df['role_understand_why_num'] == 1]['overall_fear_score'].mean(),
    df[df['role_played_myself_num'] == 1]['overall_fear_score'].mean(),
    df[df['role_played_with_kids_num'] == 1]['overall_fear_score'].mean()
]
fear_no = [
    df[df['role_understand_why_num'] == 0]['overall_fear_score'].mean(),
    df[df['role_played_myself_num'] == 0]['overall_fear_score'].mean(),
    df[df['role_played_with_kids_num'] == 0]['overall_fear_score'].mean()
]

x = np.arange(len(dimensions))
w = 0.32

b1 = ax.bar(x - w/2, fear_yes, w, label='Yes (Engaged / Empathetic)', color='#059669')
b2 = ax.bar(x + w/2, fear_no, w, label='No (Disengaged / Unfamiliar)', color='#E11D48')

ax.set_ylabel('Mean Fear Score (1 = None, 4 = High)', fontsize=11, fontweight='bold', color='#1E293B')
ax.set_title('The Empathy Buffer: Parental Participation Lowers Anxiety and Fear (p < 0.05)', fontsize=12, fontweight='bold', pad=15, color='#0F172A')
ax.set_xticks(x)
ax.set_xticklabels(dimensions, fontsize=10, fontweight='bold', color='#334155')
ax.set_ylim(2.0, 4.0)
ax.legend(frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=9.5)

for rect in b1 + b2:
    h = rect.get_height()
    ax.annotate(f'{h:.2f}', xy=(rect.get_x() + rect.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{out_dir}/chart4_empathy_buffer.png')
plt.close()

# -------------------------------------------------------------
# Chart 5: Shooter Game Anxiety vs Casual Games
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
genres = ['Fear of Violent\nBehavior (p=0.032)', 'View: Games Are\nViolent (p=0.039)', 'Fear of\nAddiction', 'Actual Family\nImpact (p=0.33)']
shooter_means = [
    df[df['has_shooter'] == 1]['fear_violence_num'].mean(),
    df[df['has_shooter'] == 1]['perc_violent_num'].mean(),
    df[df['has_shooter'] == 1]['fear_addiction_num'].mean(),
    df[df['has_shooter'] == 1]['overall_impact_score'].mean()
]
non_shooter_means = [
    df[df['has_shooter'] == 0]['fear_violence_num'].mean(),
    df[df['has_shooter'] == 0]['perc_violent_num'].mean(),
    df[df['has_shooter'] == 0]['fear_addiction_num'].mean(),
    df[df['has_shooter'] == 0]['overall_impact_score'].mean()
]

x = np.arange(len(genres))
w = 0.32

g1 = ax.bar(x - w/2, shooter_means, w, label='Shooter / Battle Royale (PUBG/FreeFire/CoD)', color='#7C3AED')
g2 = ax.bar(x + w/2, non_shooter_means, w, label='Casual / Social / Sandbox Games', color='#06B6D4')

ax.set_ylabel('Mean Score', fontsize=11, fontweight='bold', color='#1E293B')
ax.set_title('The Genre Split: Shooter Games Heighten Fear, but Family Conflict Delta is Minimal', fontsize=11, fontweight='bold', pad=15, color='#0F172A')
ax.set_xticks(x)
ax.set_xticklabels(genres, fontsize=9.5, fontweight='bold', color='#334155')
ax.set_ylim(0, 4.5)
ax.legend(frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=9)

for rect in g1 + g2:
    h = rect.get_height()
    ax.annotate(f'{h:.2f}', xy=(rect.get_x() + rect.get_width()/2, h),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=8.5, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{out_dir}/chart5_shooter_anxiety.png')
plt.close()

print("All charts successfully generated in:", out_dir)
