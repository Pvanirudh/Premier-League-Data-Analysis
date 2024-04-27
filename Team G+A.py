# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 18:03:51 2024

@author: aniru
"""
import pandas as pd
import matplotlib.pyplot as plt
# Load the data from the provided CSV file
data_path = 'squad_premier_league_stats.csv'
data = pd.read_csv(data_path)
# Get the top 10 teams with the most goals
top_goals = data.nlargest(10, 'Goals')
# Get the top 10 teams with the most assists
top_assists = data.nlargest(10, 'Assists')
# Create a figure with 2 bar plots, one for goals and one for assists
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
# Plot the top 10 teams with the most goals
top_goals.plot(kind='bar', x='Squad', y='Goals', ax=ax1, color='orange')
ax1.set_title('Top 10 Teams with Most Goals')
ax1.set_xlabel('Squad')
ax1.set_ylabel('Goals')
# Plot the top 10 teams with the most assists
top_assists.plot(kind='bar', x='Squad', y='Assists', ax=ax2, color='lightblue')
ax2.set_title('Top 10 Teams with Most Assists')
ax2.set_xlabel('Squad')
ax2.set_ylabel('Assists')
# Save the plot
output_path = 'top_teams_plot.png'
plt.tight_layout()
plt.savefig(output_path)
plt.close()