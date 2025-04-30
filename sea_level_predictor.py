import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15,6))

    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]
    ax.scatter(x = x, y = y, color="red", s=10)

    # Create first line of best fit
    line1 = linregress(x = x, y=y)
    x_valuesA = pd.Series([i for i in range(1880, 2051)])
    y_valuesA = line1.slope*x_valuesA + line1.intercept
    plt.plot(x_valuesA, y_valuesA)


    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000]
    x2 = df_2000["Year"]
    y2 = df_2000["CSIRO Adjusted Sea Level"]
    line2 = linregress(x2, y2)

    x_valuesB = pd.Series([i for i in range(2000, 2051)])
    y_valuesB = line2.slope*x_valuesB + line2.intercept
    plt.plot(x_valuesB, y_valuesB, "y")

    # Add labels and title

    ax.set_xlabel("Year") 
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()