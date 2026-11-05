import pandas as pd
import numpy as np
import scipy.stats as stats
import json

df = pd.read_csv('C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/data/survey_data.csv')

print(f"Total rows: {len(df)}")
print("Does kid play games distribution:")
print(df['Does your kid/s play online games?'].value_counts(dropna=False))

# Separate active respondents (those whose kids play games: Yes or Sometimes)
df_active = df[df['Does your kid/s play online games?'].isin(['Yes', 'Sometimes'])].copy()
print(f"Active respondents: {len(df_active)}")

# Clean column names for convenience
col_mapping = {
    'Timestamp': 'timestamp',
    'Does your kid/s play online games?': 'kid_plays_games',
    'Could you name some Online Games your kid/s play? (eg. Candy Crush, Minecraft, Call of Duty, PUBG, Counter Strike, etc.)': 'games_named',
    'What would you say to the following statements regarding online gaming? [Online Gaming can be beneficial to kids]': 'perc_beneficial',
    'What would you say to the following statements regarding online gaming? [Online Gaming is a good stress-buster]': 'perc_stress_buster',
    'What would you say to the following statements regarding online gaming? [Online Gaming is a good way for kids to socialize]': 'perc_socialize',
    'What would you say to the following statements regarding online gaming? [Online Gaming can be a profitable career for kids]': 'perc_career',
    'What would you say to the following statements regarding online gaming? [Online Gaming requires parental supervision]': 'perc_supervision',
    'What would you say to the following statements regarding online gaming? [Online Gaming can be a distraction]': 'perc_distraction',
    'What would you say to the following statements regarding online gaming? [Online Games are violent in nature]': 'perc_violent',
    'What would you say to the following statements regarding online gaming? [Online Gaming can have dangerous consequences]': 'perc_dangerous',
    'What would you say to the following statements regarding online gaming? [Online Gaming is a waste of money]': 'perc_waste_money',
    'How much fear do you hold with regard to the following aspects of Online Gaming? [Online Games can be addictive]': 'fear_addiction',
    'How much fear do you hold with regard to the following aspects of Online Gaming? [Online Games can cause violent/aggressive behaviour]': 'fear_violence',
    'How much fear do you hold with regard to the following aspects of Online Gaming? [Online Games exposes kids to age-inappropriate content]': 'fear_content',
    'How much fear do you hold with regard to the following aspects of Online Gaming? [Online Games can affect academic performance]': 'fear_academics',
    'How much fear do you hold with regard to the following aspects of Online Gaming? [Online Games can have adverse health affects]': 'fear_health',
    'Mark "True" or "False" for the following statements regarding your role in Online Gaming  [I have played Online Games myself]': 'role_played_myself',
    'Mark "True" or "False" for the following statements regarding your role in Online Gaming  [I know my kids\' favorite Online Games]': 'role_know_favorites',
    'Mark "True" or "False" for the following statements regarding your role in Online Gaming  [I understand why my kids play Online Games]': 'role_understand_why',
    'Mark "True" or "False" for the following statements regarding your role in Online Gaming  [I have sometimes played Online Games with my kids]': 'role_played_with_kids',
    'Mark "True" or "False" for the following statements regarding your role in Online Gaming  [I am not interested in playing/learning about Online Games]': 'role_not_interested',
    'Mark "True" or "False" for the following statements regarding your role in Online Gaming  [I think its necessary to place rules for kids\' Online Gaming behaviour]': 'role_rules_necessary',
    'Mark "True" or "False" for the following statements with regard to the rules you have put in place for your kids\' Online Gaming Behavior [I only allow my kid/s to play Online Games on certain days of the week]': 'rule_days_of_week',
    'Mark "True" or "False" for the following statements with regard to the rules you have put in place for your kids\' Online Gaming Behavior [I only allow my kid/s to play Online Games at certain times of the day]': 'rule_times_of_day',
    'Mark "True" or "False" for the following statements with regard to the rules you have put in place for your kids\' Online Gaming Behavior [I only allow my kid/s to play Online Games for a fixed duration of time (eg. one hour)]': 'rule_fixed_duration',
    'Mark "True" or "False" for the following statements with regard to the rules you have put in place for your kids\' Online Gaming Behavior [I do not allow my kid/s to play Online Games during exams ]': 'rule_no_exams',
    'Mark "True" or "False" for the following statements with regard to the rules you have put in place for your kids\' Online Gaming Behavior [I only allow my kid/s to play certain kinds of Online Games]': 'rule_certain_kinds',
    'Mark "True" or "False" for the following statements with regard to the rules you have put in place for your kids\' Online Gaming Behavior [I only allow my kid/s to spend a certain amount of money on Online Games]': 'rule_spending_limit',
    'Mark "True" or "False" for the following statements with regard to the rules you have put in place for your kids\' Online Gaming Behavior [I have no rules whatsoever]': 'rule_no_rules',
    'Mark the amount of impact that Online Gaming has had on the following aspects within your family [Frustrations in the family due to kids\' Online Gaming behavior]': 'impact_frustration',
    'Mark the amount of impact that Online Gaming has had on the following aspects within your family [Arguments/conflicts in the family due to kids\' Online behavior]': 'impact_conflict',
    'Mark the amount of impact that Online Gaming has had on the following aspects within your family [Strain in parent-child relationship due to kids\' Online Gaming Behavior]': 'impact_strain',
    'What is your income level? (per annum)': 'income',
    'What age group are your kid/s in?': 'kid_age_group',
    'What is your gender?': 'gender',
    'What is your occupation?': 'occupation',
    'Which city do you live in?': 'city'
}

df_active = df_active.rename(columns=col_mapping)

# Likert mapping
likert_5 = {
    'Strongly Disagree': 1,
    'Disagree': 2,
    'Neutral': 3,
    'Agree': 4,
    'Strongly Agree': 5
}

likert_fear = {
    'No fear': 1,
    'Low fear': 2,
    'Medium fear': 3,
    'High fear': 4
}

likert_impact = {
    'No Impact': 0,
    'Low Impact': 1,
    'Medium Impact': 2,
    'High Impact': 3
}

def clean_bool(val):
    if pd.isna(val):
        return np.nan
    s = str(val).strip().replace('"', '').lower()
    if s == 'true':
        return 1
    elif s == 'false':
        return 0
    return np.nan

# Map values
perc_cols = [c for c in df_active.columns if c.startswith('perc_')]
for c in perc_cols:
    df_active[c + '_num'] = df_active[c].map(likert_5)

fear_cols = [c for c in df_active.columns if c.startswith('fear_')]
for c in fear_cols:
    df_active[c + '_num'] = df_active[c].map(likert_fear)

impact_cols = [c for c in df_active.columns if c.startswith('impact_')]
for c in impact_cols:
    df_active[c + '_num'] = df_active[c].map(likert_impact)

role_cols = [c for c in df_active.columns if c.startswith('role_')]
for c in role_cols:
    df_active[c + '_num'] = df_active[c].apply(clean_bool)

rule_cols = [c for c in df_active.columns if c.startswith('rule_')]
for c in rule_cols:
    df_active[c + '_num'] = df_active[c].apply(clean_bool)

# Aggregate indices
df_active['overall_fear_score'] = df_active[[c + '_num' for c in fear_cols]].mean(axis=1)
df_active['overall_impact_score'] = df_active[[c + '_num' for c in impact_cols]].mean(axis=1)
df_active['rule_count'] = df_active[['rule_days_of_week_num', 'rule_times_of_day_num', 'rule_fixed_duration_num', 'rule_no_exams_num', 'rule_certain_kinds_num', 'rule_spending_limit_num']].sum(axis=1)
df_active['positive_perception'] = df_active[['perc_beneficial_num', 'perc_stress_buster_num', 'perc_socialize_num', 'perc_career_num']].mean(axis=1)
df_active['negative_perception'] = df_active[['perc_distraction_num', 'perc_violent_num', 'perc_dangerous_num', 'perc_waste_money_num']].mean(axis=1)

print("\n--- Summary Stats ---")
print(f"Mean Fear Score (1-4): {df_active['overall_fear_score'].mean():.2f}")
print(f"Mean Impact Score (0-3): {df_active['overall_impact_score'].mean():.2f}")
print(f"Mean Rule Count (0-6): {df_active['rule_count'].mean():.2f}")

# Output detailed summary to JSON
summary = {
    'n_total': int(len(df)),
    'n_active': int(len(df_active)),
    'n_no_games': int(len(df[df['Does your kid/s play online games?'] == 'No'])),
    'demographics': {
        'kid_age_groups': df_active['kid_age_group'].value_counts().to_dict(),
        'parent_gender': df_active['gender'].value_counts().to_dict(),
        'parent_occupation': df_active['occupation'].value_counts().to_dict(),
        'income': df_active['income'].value_counts().to_dict(),
        'cities': df_active['city'].value_counts().to_dict()
    }
}
print(json.dumps(summary, indent=2))

df_active.to_csv('C:/Users/new/.gemini/antigravity/scratch/yourdost-ba-assignment/data/cleaned_active_survey.csv', index=False)
