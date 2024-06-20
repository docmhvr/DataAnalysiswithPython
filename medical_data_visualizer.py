import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
# Add 'overweight' column
# Normalize data by making 0 always good and 1 always bad
# 1
df = pd.read_csv("medical_examination.csv")
# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)
# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    # Group and reformat the data to split it by 'cardio'
    # Draw the catplot with 'sns.catplot()'
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    # 7
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig
    # 8
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # Clean the data
    # Calculate the correlation matrix
    # Generate a mask for the upper triangle
    # Set up the matplotlib figure
    # Draw the heatmap with 'sns.heatmap()'
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    # 12
    corr = df_heat.corr()
    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    # 14
    fig, ax = plt.subplots(figsize=(12, 12))
    # 15
    sns.heatmap(corr, annot=True, mask=mask, fmt='.1f', cmap='coolwarm', square=True, linewidths=.5, ax=ax)
    # 16
    fig.savefig('heatmap.png')
    return fig


