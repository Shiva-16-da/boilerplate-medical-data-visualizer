import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    df = pd.read_csv('medical_examination.csv')
    df['overweight'] = (df['weight'] / (df['height'] / 100)**2 > 25).astype(int)
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar').fig
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    df = pd.read_csv('medical_examination.csv')
    df['overweight'] = (df['weight'] / (df['height'] / 100)**2 > 25).astype(int)
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    df = df[df['ap_lo'] <= df['ap_hi']]
    df = df[df['height'].between(df['height'].quantile(0.025), df['height'].quantile(0.975))]
    df = df[df['weight'].between(df['weight'].quantile(0.025), df['weight'].quantile(0.975))]

    corr = df.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", center=0, linewidths=.5, square=True, cbar_kws={"shrink": .45})
    fig.savefig('heatmap.png')
    return fig
