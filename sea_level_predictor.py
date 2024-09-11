import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]


    # Create scatter plot
    fig , ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    r = linregress(x,y)
    print(r)
    x_p = pd.Series([i for i in range(1880,2051)])
    y_p = r.slope*x_p + r.intercept
    plt.plot(x_p, y_p, "r")

    # Create second line of best fit
    n_df = df.loc[df['Year'] >= 2000]
    n_x = n_df['Year']
    n_y = n_df["CSIRO Adjusted Sea Level"]
    r2 = linregress(n_x,n_y)
    x_p2 = pd.Series([i for i in range(2000,2051)])
    y_p2 = r2.slope*x_p2 + r2.intercept
    plt.plot(x_p2, y_p2, "g")

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()