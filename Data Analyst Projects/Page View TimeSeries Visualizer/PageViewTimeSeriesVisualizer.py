import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates = ['date'] ,index_col='date')

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) &  (df['value'] >= df['value'].quantile(0.025))]

def draw_line_plot():
  # Draw line plot
  fig, ax = plt.subplots(figsize=(10,5))
  ax.plot(df.index, df['value'], 'r', linewidth = 1)
  plt.xlabel('Date')
  plt.ylabel('Page Views')
  plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  
  # Save image and return fig (don't change this part)
  fig.savefig('line_plot.png')

  return fig

def draw_bar_plot():
  # Mouths selection with methods because of the parse done
  df["month"] = df.index.month
  df["year"] = df.index.year
  # transform to access as indices
  df_bar = df.groupby(["year","month"])["value"].mean()
  df_bar = df_bar.unstack()

  #plotting, usa plt
  fig = df_bar.plot.bar(legend=True, figsize = (10,5), ylabel='Average Page Views', xlabel='Years').figure
  plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

  # Save image and return fig (don't change this part)
  plt.savefig('bar_plot.png')
  return fig

def draw_box_plot():
  # Prepare data for box plots
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df["year"] = [d.year for d in df_box.date]
  df["month"] = [d.strftime('%b') for d in df_box.date]
  df_box['month_num'] = df_box["date"].dt.month
  df_box = df_box.sort_values('month_num')

  # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1,2,figsize=(16, 8)) 

  # for year 
  axes[0] = sns.boxplot(x=df_box['year'], y=df_box['value'], ax=axes[0]);
  axes[0].set_xlabel('Year')
  axes[0].set_ylabel('Page Views')
  axes[0].set_title('Year-wise Box Plot (Trend)')
  #for months
  axes[1] = sns.boxplot(x = df_box['month'],y = df_box['value'], ax=axes[1], order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov', 'Dec'])
  axes[1].set_xlabel('Month')
  axes[1].set_ylabel('Page Views')
  axes[1].set_title('Month-wise Box Plot (Seasonality)')
  # Save image and return fig (don't change this part)
  plt.tight_layout()
  plt.savefig('box_plot.png')
 
  return fig

# Test your function by calling it here
draw_line_plot()
draw_bar_plot()
draw_box_plot()
