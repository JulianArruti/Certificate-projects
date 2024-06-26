import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['overweight'] = np.where(df['weight']/(df['height']/100)**2 > 25, 1, 0)
df['gluc'] = df['gluc'].map({1: 0, 2: 1, 3: 1})
df['cholesterol'] = df['cholesterol'].map({1: 0, 2: 1, 3: 1})

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    melt_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=melt_vars, var_name='variable', value_name='value')

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    #df_cat.rename(columns={'value': 'condition'}, inplace=True)
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable' , 'value'], as_index = False).count()

    # Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', y= 'total',hue='value', col='cardio', data=df_cat, kind='bar').fig


    # Get the figure for the output
    fig = fig.figure

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) & 
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) & 
        (df['weight'] <= df['weight'].quantile(0.975))]
    

    # Calculate the correlation matrix
    corr = df_heat.corr(method='pearson')

    # Generate a mask for the upper triangle
    mask = np.triu(corr)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, cmap='coolwarm', annot=True, fmt='.1f', center=0.08, square=True, linewidths=0.5, cbar_kws={'shrink': 0.5}, annot_kws={'fontsize': 8})

    fig.savefig('heatmap.png')
    return fig

draw_cat_plot()
draw_heat_map()
