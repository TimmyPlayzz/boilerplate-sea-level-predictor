import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='b', label='Original Data')

    # Create first line of best fit (from 1880 to 2050)
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series([i for i in range(df['Year'].min(), 2051)])
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (from 2000 to 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent_pred = pd.Series([i for i in range(2000, 2051)])
    y_recent_pred = res_recent.slope * x_recent_pred + res_recent.intercept
    plt.plot(x_recent_pred, y_recent_pred, 'g', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()