import pandas as pd
import tkinter as tk
from tkinter import ttk
# Load the CSV file (ensure the path is correct)
data = pd.read_csv("player_premier_league_stats.csv")
# Correct common club name discrepancies
club_name_corrections = {
    'Newcastle Utd': 'Newcastle United',
    'Tottenham': 'Tottenham Hotspur',
    'Spurs': 'Tottenham Hotspur',
    'Leicester': 'Leicester City',
    'Man City': 'Manchester City',
    'Man Utd': 'Manchester United',
    'Nott\'ham Forest': 'Nottingham Forest',
    'West Ham': 'West Ham United',
    'Brighton': 'Brighton & Hove Albion',
    'Everton FC': 'Everton',
    # Add more corrections as needed
}
# Apply the corrections to the 'Squad' column
data['Squad'] = data['Squad'].replace(club_name_corrections)
# Function to retrieve team members and their ages
def get_team_members(club):
    club_members = data[data['Squad'] == club][['Player', 'Age', 'Pos', 'Goals', 'Assist']]
    return club_members
# Create the GUI
def create_gui():
    # Main window
    root = tk.Tk()
    root.title("Club Team Members")
    # Get unique clubs for the dropdown
    clubs = sorted(data['Squad'].unique())  # Sort the club names for the dropdown
    # Function to update the table when a club is selected
    def update_table(event):
        selected_club = club_var.get()  # Get selected club name
        team_members = get_team_members(selected_club)  # Retrieve club members
        # Clear the existing table content
        for row in table.get_children():
            table.delete(row)
        # Insert new data into the table
        for _, row in team_members.iterrows():
            table.insert("", "end", values=(row['Player'], row['Age'], row['Pos'], row['Goals'], row['Assist']))
    # Dropdown for selecting the club
    club_var = tk.StringVar(root)
    club_dropdown = ttk.Combobox(root, textvariable=club_var, values=clubs)
    club_dropdown.current(0)  # Default to the first club
    club_dropdown.grid(row=0, column=0, padx=10, pady=10)
    # Bind the dropdown selection change to update the table
    club_dropdown.bind("<<ComboboxSelected>>", update_table)
    
    # Create a table to display the team members and their ages
    table = ttk.Treeview(root, columns=("Player", "Age", "Pos", "Goals", "Assist"), show="headings")
    table.heading("Player", text="Player")
    table.heading("Age", text="Age")
    table.heading("Pos", text="Pos")
    table.heading("Goals", text="Goals")
    table.heading("Assist", text="Assist")
    table.grid(row=1, column=0, padx=10, pady=10)

    # Initial update for the first club in the dropdown
    update_table(None)
    # Start the Tkinter event loop
    root.mainloop()
# Run the GUI
create_gui()