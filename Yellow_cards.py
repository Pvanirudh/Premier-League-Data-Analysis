import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
file_path = "epl_results_2022-23.csv"
data = pd.read_csv(file_path)
# Extracting relevant data
yellow_cards = data.groupby('HomeTeam')['HY'].sum() + data.groupby('AwayTeam')['AY'].sum()
yellow_cards = yellow_cards.reset_index()
yellow_cards.columns = ['Team', 'Total_Yellow_Cards']
# Create a bar plot with improved aesthetics
plt.figure(figsize=(12, 6))
sns.set(style='whitegrid', context='talk')
# Use a more vibrant color palette
color_palette = sns.color_palette('coolwarm', n_colors=len(yellow_cards))
# Create the bar plot with the new style and palette
sns.barplot(
    x='Team',
    y='Total_Yellow_Cards',
    data=yellow_cards,
    order=yellow_cards.sort_values('Total_Yellow_Cards', ascending=False)['Team'],
    palette=color_palette
)
# Add labels and gridlines for clarity
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel("Team", fontsize=14)
plt.ylabel("Total Yellow Cards", fontsize=14)
plt.title("Total Yellow Cards for Each Team in the 2022-2023 Premier League Season", fontsize=16)
# Add a grid for better visualization
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
# Adjust the layout to make sure labels don't get cut off
plt.tight_layout()
# Save the plot as a JPG image
plt.savefig("Fouls_teams.jpg", format='jpg', dpi=300)  # Save the plot





