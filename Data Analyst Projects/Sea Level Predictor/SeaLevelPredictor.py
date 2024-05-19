import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit using linregress
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = np.arange(1880, 2051)  # Years from 1880 to 2050
    line_fit = res.intercept + res.slope * years
    plt.plot(years, line_fit, 'r', label='Best Fit Line 1880-2050')

    # Create second line of best fit using data from year 2000 to the most recent year
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(df_recent['Year'].min(), 2051)  # Years from the most recent year to 2050
    line_fit_recent = res_recent.intercept + res_recent.slope * years_recent
    plt.plot(years_recent, line_fit_recent, 'g', label='Best Fit Line 2000-Present')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()