# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:10:52 2024

@author: aniru
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def load_data():
    # Load the dataset
    data_path = 'player_premier_league_shooting.csv'
    shooting_data = pd.read_csv(data_path)
    return shooting_data
def create_penalty_chart(shooting_data):
    # Select top 10 players based on penalty attempts
    goals_scored = shooting_data.nlargest(10, 'Goals')[['Player', 'Goals']]
    # Generate a colorful bar chart
    plt.figure(figsize=(12, 8))
    colors = sns.color_palette('hsv', n_colors=goals_scored['Player'].nunique())  # Generating unique colors
    bar_plot = sns.barplot(x='Goals', y='Player', data=goals_scored, palette=colors)
    # Enhance chart visual
    plt.title('Top 10 Premier League Players by Goals (Season 2022-2023)')
    plt.xlabel('Numbers of Goals')
    plt.ylabel('Player')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    # Save the figure
    plt.savefig('Goals Scored.jpg', format='jpg', dpi=300)
    plt.close()
def main():
    shooting_data = load_data()
    create_penalty_chart(shooting_data)
if __name__ == "__main__":
    main()













