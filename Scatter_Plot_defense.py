import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import Normalize
import numpy as np
# Load the data
data_path = "defensive_premier_league_stats.csv"
defensive_data = pd.read_csv(data_path)
# Function to generate a scatter plot and manually adjust text labels to avoid overlap
def generate_scatter_plot_with_adjusted_labels(data, x_col, y_col, title, x_label, y_label, figsize=(12, 8)):
    plt.figure(figsize=figsize)
    colors = plt.cm.tab20(np.linspace(0, 1, len(data['Squad'].unique())))  # Define color palette
    # Plot the scatter points with unique colors
    scatter = plt.scatter(data[x_col], data[y_col], c=[colors[i % len(colors)] for i in range(len(data))], s=100, alpha=0.7)
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
    # Manually add text labels with slight adjustments to avoid overlap
    label_offsets = {  # Define offsets for text labels to reduce overlap
        'right': 0.5,
        'left': -0.5,
        'up': 0.5,
        'down': -0.5
    }
    for i in range(len(data)):
        # Add squad name as text with slight adjustments
        x_pos = data[x_col].iloc[i]
        y_pos = data[y_col].iloc[i]
        if x_pos < mean_x:
            x_offset = label_offsets['left']
        else:
            x_offset = label_offsets['right']
        if y_pos < mean_y:
            y_offset = label_offsets['down']
        else:
            y_offset = label_offsets['up']
        plt.text(
            x_pos + x_offset, y_pos + y_offset,
            data['Squad'].iloc[i], color='white', ha='center', va='center'
        )
    # Additional styling
    plt.grid(False)
    plt.tick_params(colors='white', which='both')
    plt.xticks(rotation=45, ha='right')
    # Save the scatter plot in JPEG format
    output_path = "scatter_plot_with_manual_adjusted_labels2.jpg"
    plt.savefig(output_path, format='jpg', dpi=300)
    return output_path
# Generate the scatter plot with manually adjusted text labels
scatter_plot_with_manual_adjusted_labels_path = generate_scatter_plot_with_adjusted_labels(
    defensive_data,
    x_col='TklW',  # 'Tackles Won'
    y_col='Int',  # 'Interceptions'
    title='Tackles Won vs Intercepts by Team - Premier League Season 2022-2023',
    x_label='Tackles Won',
    y_label='Interceptions'
)
print(f"Scatter plot with adjusted labels saved at: {scatter_plot_with_manual_adjusted_labels_path}")