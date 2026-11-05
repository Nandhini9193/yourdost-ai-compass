import pandas as pd
import numpy as np
import scipy.stats as stats
import sys

sys.stdout.reconfigure(encoding='utf-8')

import os
base_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(base_dir, 'cleaned_active_survey.csv'))

print("="*60)
print("INCOME BREAKDOWN")
print("="*60)
income_order = [
    'Less than ₹70,000',
    'Between ₹70,000 and ₹2,70,000',
    'Between ₹2,70,000 and ₹8,45,000',
    'More than ₹8,45,000'
]
for inc in income_order:
    sub = df[df['income'] == inc]
    print(f"Income: {inc} (n={len(sub)})")
    print(f"  Fear Score: {sub['overall_fear_score'].mean():.2f}")
    print(f"  Impact Score: {sub['overall_impact_score'].mean():.2f}")
    print(f"  Frustration: {sub['impact_frustration_num'].mean():.2f}")
    print(f"  Conflict: {sub['impact_conflict_num'].mean():.2f}")
    print(f"  Strain: {sub['impact_strain_num'].mean():.2f}")
    print(f"  Rule count: {sub['rule_count'].mean():.2f}")
    print(f"  Spending limit rule %: {(sub['rule_spending_limit_num']==1).mean()*100:.1f}%")

print("\n" + "="*60)
print("OCCUPATION BREAKDOWN")
print("="*60)
for occ, sub in df.groupby('occupation'):
    if len(sub) >= 5:
        print(f"Occupation: {occ} (n={len(sub)})")
        print(f"  Fear Score: {sub['overall_fear_score'].mean():.2f} | Impact: {sub['overall_impact_score'].mean():.2f} | Rules: {sub['rule_count'].mean():.2f}")

print("\n" + "="*60)
print("SCHOOL AGE (6-12) DEEP DIVE")
print("="*60)
school_df = df[df['kid_age_group'] == 'School Age (6-12 years old)']
print(f"School age (6-12) total: {len(school_df)}")
print(f"  Overall impact: {school_df['overall_impact_score'].mean():.2f} (vs non-school: {df[df['kid_age_group'] != 'School Age (6-12 years old)']['overall_impact_score'].mean():.2f})")
print(f"  Frustration: {school_df['impact_frustration_num'].mean():.2f} (vs {df[df['kid_age_group'] != 'School Age (6-12 years old)']['impact_frustration_num'].mean():.2f})")
print(f"  Conflict: {school_df['impact_conflict_num'].mean():.2f} (vs {df[df['kid_age_group'] != 'School Age (6-12 years old)']['impact_conflict_num'].mean():.2f})")
print(f"  Strain: {school_df['impact_strain_num'].mean():.2f} (vs {df[df['kid_age_group'] != 'School Age (6-12 years old)']['impact_strain_num'].mean():.2f})")
t_stat, p_val = stats.ttest_ind(school_df['overall_impact_score'].dropna(), df[df['kid_age_group'] != 'School Age (6-12 years old)']['overall_impact_score'].dropna())
print(f"  T-test for School Age Impact vs Others: t={t_stat:.2f}, p-value={p_val:.4f}")

# What games do School Age kids play?
print("\nGames played by School Age kids:")
print(school_df['games_named'].value_counts().head(10))

print("\n" + "="*60)
print("PARENTAL ARCHETYPES / CLUSTERING")
print("="*60)
# Let's see combinations of: Played with kids (Yes/No) and Rule count (High >= 3 vs Low < 3)
df['engaged_partner'] = (df['role_played_with_kids_num'] == 1) & (df['role_understand_why_num'] == 1)
df['distant_disciplinarian'] = (df['role_played_with_kids_num'] == 0) & (df['rule_count'] >= 3)
df['detached_lenient'] = (df['role_played_with_kids_num'] == 0) & (df['rule_count'] < 3)
df['co_player_high_rules'] = (df['role_played_with_kids_num'] == 1) & (df['rule_count'] >= 3)
df['co_player_low_rules'] = (df['role_played_with_kids_num'] == 1) & (df['rule_count'] < 3)

for arch in ['engaged_partner', 'distant_disciplinarian', 'detached_lenient', 'co_player_high_rules', 'co_player_low_rules']:
    sub = df[df[arch] == True]
    print(f"Archetype {arch:25s} (n={len(sub)}): Impact={sub['overall_impact_score'].mean():.2f}, Fear={sub['overall_fear_score'].mean():.2f}, Strain={sub['impact_strain_num'].mean():.2f}")

