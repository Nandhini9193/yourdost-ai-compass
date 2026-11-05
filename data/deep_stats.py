import pandas as pd
import numpy as np
import scipy.stats as stats

df = pd.read_csv('C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/data/cleaned_active_survey.csv')

print("="*60)
print("1. THE COGNITIVE DISSONANCE: PERCEPTIONS VS FEARS")
print("="*60)
perc_cols = ['perc_beneficial_num', 'perc_stress_buster_num', 'perc_socialize_num', 'perc_career_num',
             'perc_supervision_num', 'perc_distraction_num', 'perc_violent_num', 'perc_dangerous_num', 'perc_waste_money_num']
for col in perc_cols:
    agree_pct = (df[col] >= 4).mean() * 100
    mean_val = df[col].mean()
    print(f"{col:25s}: Mean={mean_val:.2f}, Agree/Strongly Agree={agree_pct:.1f}%")

print("\nFears breakdown (1=No fear, 4=High fear):")
fear_cols = ['fear_addiction_num', 'fear_violence_num', 'fear_content_num', 'fear_academics_num', 'fear_health_num']
for col in fear_cols:
    high_fear_pct = (df[col] == 4).mean() * 100
    med_high_pct = (df[col] >= 3).mean() * 100
    mean_val = df[col].mean()
    print(f"{col:25s}: Mean={mean_val:.2f}, High fear={high_fear_pct:.1f}%, Med+High={med_high_pct:.1f}%")

print("\n" + "="*60)
print("2. GAMER PARENTS VS NON-GAMER PARENTS")
print("="*60)
print("Role distributions:")
for col in ['role_played_myself_num', 'role_know_favorites_num', 'role_understand_why_num', 'role_played_with_kids_num', 'role_not_interested_num']:
    print(f"{col}: {df[col].value_counts(normalize=True).to_dict()}")

# Compare parents who played with kids vs those who didn't
p_with_kids = df[df['role_played_with_kids_num'] == 1]
p_without_kids = df[df['role_played_with_kids_num'] == 0]

print(f"\nParents played with kids (n={len(p_with_kids)}) vs didn't (n={len(p_without_kids)}):")
for metric in ['overall_fear_score', 'overall_impact_score', 'impact_frustration_num', 'impact_conflict_num', 'impact_strain_num', 'positive_perception', 'negative_perception', 'rule_count']:
    m1 = p_with_kids[metric].mean()
    m2 = p_without_kids[metric].mean()
    t_stat, p_val = stats.ttest_ind(p_with_kids[metric].dropna(), p_without_kids[metric].dropna())
    u_stat, u_pval = stats.mannwhitneyu(p_with_kids[metric].dropna(), p_without_kids[metric].dropna())
    print(f"{metric:25s}: With={m1:.2f} | Without={m2:.2f} | t={t_stat:.2f}, p={p_val:.4f} | MW-U p={u_pval:.4f}")

# Compare parents who played games themselves vs didn't
p_played = df[df['role_played_myself_num'] == 1]
p_not_played = df[df['role_played_myself_num'] == 0]
print(f"\nParents who played themselves (n={len(p_played)}) vs didn't (n={len(p_not_played)}):")
for metric in ['overall_fear_score', 'overall_impact_score', 'impact_strain_num', 'rule_count', 'positive_perception']:
    m1 = p_played[metric].mean()
    m2 = p_not_played[metric].mean()
    t_stat, p_val = stats.ttest_ind(p_played[metric].dropna(), p_not_played[metric].dropna())
    print(f"{metric:25s}: Played={m1:.2f} | NotPlayed={m2:.2f} | p={p_val:.4f}")

# Compare parents who 'understand why kids play'
p_und = df[df['role_understand_why_num'] == 1]
p_not_und = df[df['role_understand_why_num'] == 0]
print(f"\nParents who understand why (n={len(p_und)}) vs don't (n={len(p_not_und)}):")
for metric in ['overall_impact_score', 'impact_strain_num', 'overall_fear_score']:
    m1 = p_und[metric].mean()
    m2 = p_not_und[metric].mean()
    t_stat, p_val = stats.ttest_ind(p_und[metric].dropna(), p_not_und[metric].dropna())
    print(f"{metric:25s}: Understand={m1:.2f} | Don't={m2:.2f} | p={p_val:.4f}")

print("\n" + "="*60)
print("3. THE RULE PARADOX: DO RULES REDUCE CONFLICT OR CORRELATE WITH HIGHER FRICTION?")
print("="*60)
# Correlation between rule_count and impact
corr_rule_impact, p_rule_impact = stats.spearmanr(df['rule_count'].dropna(), df['overall_impact_score'].dropna())
print(f"Spearman correlation between Rule Count and Family Impact: rho={corr_rule_impact:.3f}, p={p_rule_impact:.4f}")

rule_cols = ['rule_days_of_week_num', 'rule_times_of_day_num', 'rule_fixed_duration_num', 'rule_no_exams_num', 'rule_certain_kinds_num', 'rule_spending_limit_num', 'rule_no_rules_num']
for rcol in rule_cols:
    r_has = df[df[rcol] == 1]
    r_no = df[df[rcol] == 0]
    if len(r_has) > 0 and len(r_no) > 0:
        imp_has = r_has['overall_impact_score'].mean()
        imp_no = r_no['overall_impact_score'].mean()
        strain_has = r_has['impact_strain_num'].mean()
        strain_no = r_no['impact_strain_num'].mean()
        t_stat, p_val = stats.ttest_ind(r_has['overall_impact_score'].dropna(), r_no['overall_impact_score'].dropna())
        print(f"{rcol:25s} (Yes n={len(r_has)}, No n={len(r_no)}): Impact Has={imp_has:.2f} vs No={imp_no:.2f} (p={p_val:.4f}) | Strain Has={strain_has:.2f} vs No={strain_no:.2f}")

print("\n" + "="*60)
print("4. AGE GROUP DYNAMICS")
print("="*60)
print(df.groupby('kid_age_group')[['overall_impact_score', 'impact_frustration_num', 'impact_conflict_num', 'impact_strain_num', 'overall_fear_score', 'rule_count']].mean())
print("\nCount per age group:")
print(df['kid_age_group'].value_counts())

# ANOVA across age groups for impact
groups = [group['overall_impact_score'].dropna() for _, group in df.groupby('kid_age_group') if len(group) >= 5]
f_val, p_val = stats.f_oneway(*groups)
print(f"\nANOVA across age groups for Family Impact: F={f_val:.2f}, p={p_val:.4f}")

print("\n" + "="*60)
print("5. GAME TYPE / GENRE ANALYSIS")
print("="*60)
# Tag games as Shooter/Action/Violent (PUBG, Free Fire, Call of Duty, Counter Strike, etc.) vs Casual
def is_shooter(text):
    if pd.isna(text):
        return 0
    t = str(text).lower()
    shooter_keywords = ['pubg', 'free fire', 'freefire', 'call of duty', 'counter strike', 'brawhalla', 'mortal kombat']
    return 1 if any(k in t for k in shooter_keywords) else 0

def is_casual_social(text):
    if pd.isna(text):
        return 0
    t = str(text).lower()
    casual_keywords = ['candy crush', 'ludo', 'among us', 'minecraft', 'talking tom', 'psych', 'subway surfer', 'mario', 'sims', 'clash of clans', 'fifa']
    return 1 if any(k in t for k in casual_keywords) else 0

df['has_shooter'] = df['games_named'].apply(is_shooter)
df['has_casual'] = df['games_named'].apply(is_casual_social)

print(f"Shooter games reported: {df['has_shooter'].sum()} out of {len(df)}")
sh_yes = df[df['has_shooter'] == 1]
sh_no = df[df['has_shooter'] == 0]
for metric in ['overall_impact_score', 'fear_violence_num', 'fear_addiction_num', 'perc_violent_num', 'perc_dangerous_num']:
    m1 = sh_yes[metric].mean()
    m2 = sh_no[metric].mean()
    t_stat, p_val = stats.ttest_ind(sh_yes[metric].dropna(), sh_no[metric].dropna())
    print(f"{metric:25s}: Shooter={m1:.2f} | Non-Shooter={m2:.2f} | p={p_val:.4f}")

print("\n" + "="*60)
print("6. GENDER AND INCOME DIFFERENCES")
print("="*60)
print(df.groupby('gender')[['overall_fear_score', 'overall_impact_score', 'rule_count']].mean())
print(df.groupby('income')[['overall_fear_score', 'overall_impact_score', 'rule_count']].mean())

