# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:42:24 2024

@author: aniru
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc
import pandas as pd
# Load the data
data = pd.read_csv('defensive_premier_league_stats.csv')
# Normalize "Tkl+Int" values for heatmap intensity
data['Normalized Tkl+Int'] = (data['Tkl+Int'] - data['Tkl+Int'].min()) / (data['Tkl+Int'].max() - data['Tkl+Int'].min())
# Function to draw a football field
def draw_field(ax):
    # Set the background to green to resemble a football field
    field_color = 'green'
    ax.set_facecolor(field_color)
    # Draw the field outline and center line
    ax.add_patch(Rectangle((-50, -30), 100, 60, edgecolor="white", facecolor="none", lw=2))
    ax.plot([0, 0], [-30, 30], color="white")
    # Penalty areas
    ax.add_patch(Rectangle((-50, -12), 16, 24, edgecolor="white", facecolor="none", lw=2))
    ax.add_patch(Rectangle((34, -12), 16, 24, edgecolor="white", facecolor="none", lw=2))
    # Center circle
    ax.add_patch(Arc((0, 0), 20, 20, theta1=0, theta2=360, color="white", lw=2))
    # Remove ticks and labels
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-50, 50)
    ax.set_ylim(-30, 30)
# Function to create a heatmap over the football field
def create_heatmap(data, ax):
    # Generate random positions for the heatmap dots within the field boundaries
    x_positions = np.random.normal(0, 20, size=len(data))  # X positions spread around the center
    y_positions = np.random.normal(0, 15, size=len(data))  # Y positions spread along the length
    # Use a color map in warm colors and plot with varying sizes based on normalized values
    colors = plt.cm.hot(data['Normalized Tkl+Int'])
    scatter = ax.scatter(x_positions, y_positions, c=data['Normalized Tkl+Int'], s=500, cmap='hot', alpha=0.6)
    # Add a color bar for reference
    plt.colorbar(scatter, ax=ax, orientation='horizontal', pad=0.01, label='Tkl+Int Normalized')
# Main function to generate and save the plot
def main():
    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 7))
    draw_field(ax)
    create_heatmap(data, ax)
    # Save the plot as a JPEG file
    plt.savefig('football_field_heatmap.jpg', format='jpg', dpi=300)
    plt.show()
# Execute the main function
main()




















