import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import Normalize
import numpy as np
# Load the data from the CSV file
data_path = "defensive_premier_league_stats.csv"  # Update with the correct CSV file path
defensive_data = pd.read_csv(data_path)
# Function to generate a scatter plot with squad name labels
def generate_scatter_plot_with_labels(data, x_col, y_col, title, x_label, y_label, figsize=(12, 8)):
    plt.figure(figsize=figsize)
    colors = plt.cm.tab20(np.linspace(0, 1, len(data['Squad'].unique())))  # Define color palette
    # Plot the scatter points with squad name labels
    for i in range(len(data)):
        # Plot each point with a color from the defined palette
        plt.scatter(
            data[x_col].iloc[i], data[y_col].iloc[i],
            c=[colors[i % len(colors)]], s=100, alpha=0.7
        )
        # Add text for the squad name
        plt.text(
            data[x_col].iloc[i], data[y_col].iloc[i], data['Squad'].iloc[i],
            color='white', ha='center', va='bottom'
        )
    # Set a black background and white reference lines at the mean for x and y axes
    plt.gca().set_facecolor('#363636')
    plt.gcf().set_facecolor('#363636')
    plt.title(title, color='white')
    plt.xlabel(x_label, color='white')
    plt.ylabel(y_label, color='white')
    mean_x = data[x_col].mean()
    mean_y = data[y_col].mean()
    plt.axvline(mean_x, color='white', linestyle='--', linewidth=2)
    plt.axhline(mean_y, color='white', linestyle='--', linewidth=2)
    # Additional styling
    plt.grid(False)
    plt.tick_params(colors='white', which='both')
    # Save the scatter plot in JPEG format
    output_path = "scatter_plot_with_squad_labels.jpg"
    plt.savefig(output_path, format='jpg', dpi=300)  # Save in JPEG format
    return output_path
# Generate a scatter plot with 'TklW' and 'Int', showing squad names
scatter_plot_with_labels_path = generate_scatter_plot_with_labels(
    defensive_data,
    x_col='TklW',  # 'Tackles Won'
    y_col='Int',  # 'Interceptions'
    title='Tackles Won vs Intercepts by Team - Premier League Season 2022-2023',
    x_label='Tackles Won',
    y_label='Interceptions'
)







