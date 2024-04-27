# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:10:52 2024

@author: aniru
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def load_data(data_path):
    # Load the dataset from the specified path
    defensive_data = pd.read_csv(data_path)
    return defensive_data
def generate_defensive_chart_with_scale(data, output_path, figsize=(12, 12), x_axis_rotation=90, y_axis_min=0, y_axis_max=None):
    # Get the top 10 teams with the most tackles and interceptions (Tkl+Int)
    top_10_teams = data.nlargest(10, 'Tkl+Int')[['Squad', 'Tkl+Int']]
    # Set the maximum value for the y-axis if not provided
    if y_axis_max is None:
        y_axis_max = top_10_teams['Tkl+Int'].max() + 50  # Adding a buffer to the max value
    # Create a colorful bar chart with unique colors for each squad
    plt.figure(figsize=figsize)
    colors = sns.color_palette('hsv', n_colors=top_10_teams['Squad'].nunique())  # Unique colors
    bar_plot = sns.barplot(x='Squad', y='Tkl+Int', data=top_10_teams, palette=colors)
    # Enhance chart visuals
    plt.title('Top 10 Teams with Most Tackles and Interceptions (Season 2022-2023)')
    plt.xlabel('Squad')
    plt.ylabel('Tackles and Interceptions')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add grid with a light style
    plt.xticks(rotation=x_axis_rotation)  # Rotate x-axis labels to vertical
    plt.ylim(y_axis_min, y_axis_max)  # Set the y-axis scale
    # Save the figure with specified resolution and format
    plt.savefig(output_path, format='jpg', dpi=300)
    plt.close()  # Close the plot to avoid display-related issues
    return output_path  # Return the path to the saved chart
# Load the dataset from the previously uploaded file
data_path = "defensive_premier_league_stats.csv"
defensive_data = load_data(data_path)
# Define the output path for the saved chart
output_chart_path = "defensive_tackles_interceptions_bar_chart_with_scale.jpg"
# Generate the bar chart with a specific y-axis scale and vertical x-axis labels
chart_path = generate_defensive_chart_with_scale(defensive_data, output_chart_path)
# Return the path to the saved chart
print(f"Chart saved at: {chart_path}")













