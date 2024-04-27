import sys
import pandas as pd
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QComboBox, QTableWidget, QTableWidgetItem
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
# Function to set the background image for a widget
def set_background(widget, image_path):
    background_label = QLabel(widget)
    pixmap = QPixmap(image_path)
    background_label.setPixmap(pixmap.scaled(1920, 1080, Qt.IgnoreAspectRatio))
    background_label.setGeometry(0, 0, 1920, 1080)
    background_label.lower()  # Ensures it's the background
# Define the NewWindow class for general windows
class NewWindow(QMainWindow):
    def __init__(self, title, background_image_path):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 1920, 1080)  # Full HD resolution
        set_background(self, background_image_path)
        self.initUI(title)
    def initUI(self, title):
        self.label = QLabel("This is the content for: " + title, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(710, 490, 500, 100)  # Centered within 1920x1080
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.back_button.clicked.connect(self.close)
        self.back_button.setGeometry(10, 10, 60, 30)  # Back button
        self.back_button.setStyleSheet("QPushButton { color: white; background-color: #333; }")
# Define the CSVDataDisplayApp class for displaying CSV data
class CSVDataDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team Stats Table")
        self.resize(1920, 1080)  # Full HD resolution
        self.initUI()
    def initUI(self):
        # Load the CSV data
        csv_path = "shooting_premier_league_stats.csv"
        self.data = pd.read_csv(csv_path)
        # Main layout
        layout = QVBoxLayout()
        # Dropdown to select teams
        self.dropdown = QComboBox()
        self.dropdown.addItems(self.data['Squad'].unique())  # Unique team names
        self.dropdown.currentIndexChanged.connect(self.update_table)  # Connect to update function
        layout.addWidget(self.dropdown)
        # Table to display team data
        self.table = QTableWidget()
        layout.addWidget(self.table)
        # Update the table with the initially selected team
        self.update_table()
        # Main widget to contain the layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        # Back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.back_button.clicked.connect(self.close)
        self.back_button.setGeometry(10, 1000, 60, 30)
        self.back_button.setStyleSheet("QPushButton { color: white; background-color: #333; }")
    def update_table(self):
        selected_team = self.dropdown.currentText()
        # Filter data for the selected team
        team_data = self.data[self.data['Squad'] == selected_team]
        # Update the table's column count and headers
        self.table.setColumnCount(len(team_data.columns))
        self.table.setHorizontalHeaderLabels(team_data.columns.tolist())
        # Update the table's row count and populate with data
        self.table.setRowCount(len(team_data))
        for i, row in enumerate(team_data.values):
            for j, cell in enumerate(row):
                item = QTableWidgetItem(str(cell))
                self.table.setItem(i, j, item)
        # Enable table features
        self.table.setSortingEnabled(True)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Stretch columns
        self.table.verticalHeader().setDefaultSectionSize(30)  # Row height adjustment
        self.table.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #fff;")
# Define the PlotWindow class for displaying plots
class PlotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plot Display")
        self.setGeometry(100, 100, 800, 600)  # Window geometry
        self.display_plot()
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.back_button.clicked.connect(self.close)  # Set button to close
        self.back_button.setGeometry(10, 10, 60, 30)  # Button position
        self.back_button.setStyleSheet("QPushButton { color: white; background-color: #333; }")
    def display_plot(self):
        label = QLabel(self)
        pixmap = QPixmap("top_teams_plot.png")  # Load the plot image
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)  # Center the image
        self.setCentralWidget(label)
# Functions to create specific windows
def create_season_stats_window():
    plot_window = PlotWindow()  # Create a new plot window
    plot_window.show()  # Show the window
    open_windows.append(plot_window)
def create_team_stats_window():
    csv_window = CSVDataDisplayApp()  # Create a CSV data display window
    csv_window.show()  # Show the window
    open_windows.append(csv_window)  # Add to the list of open windows
# Ensure all functions for buttons are defined
def create_player_comparison_window():
    new_window = NewWindow("Player Comparison", "path_to_player_comparison_background.jpg")  # Set a valid background
    new_window.show()  # Show the window
    open_windows.append(new_window)  # Add to open windows list
def create_standings_weekly_window():
    new_window = NewWindow("Weekly Standings", "path_to_standings_weekly_background.jpg")  # Update the correct path
    new_window.show()  # Show the window
    open_windows.append(new_window)  # Add to open windows list
def create_team_info_window():
    new_window = NewWindow("Team Info", "path_to_team_info_background.jpg")  # Set a valid background
    new_window.show()  # Show the window
    open_windows.append(new_window)  # Add to open windows list
# Define the WelcomeScreen class for the welcome screen
class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1920, 1080)  # Full HD resolution
        set_background(self, "premier league gif.gif")  # Animated background
        self.setupUI()  # Initialize UI components
    def setupUI(self):
        layout = QVBoxLayout(self)  # Use a layout for the screen
        start_button = QPushButton("Click to Start", self)
        start_button.setFont(QFont("Arial", 12, QFont.Bold))
        start_button.setGeometry(860, 800, 200, 50)  # Centered position
        start_button.clicked.connect(self.open_dashboard)  # Connect the event
        layout.addWidget(start_button)  # Add to layout
    def open_dashboard(self):
        self.close()  # Close the welcome screen
        main_window.show()  # Show the main window
# Initialize the application
app = QApplication(sys.argv)  # Define the application
# Main dashboard setup
main_window = QWidget()  # Define the main window
main_window.setWindowTitle("Premier League Dashboard")
set_background(main_window, "path_to_home_background.jpg")  # Set a valid path for the background
layout = QVBoxLayout(main_window)  # Layout for the main window
# List of buttons and their respective functions
button_texts = ["Season Stats", "Team Stats", "Player Comparison", "Weekly Standings", "Team Info"]
button_functions = [
    create_season_stats_window,
    create_team_stats_window,
    create_player_comparison_window,
    create_standings_weekly_window,
    create_team_info_window
]
# Add buttons to the main dashboard
for text, function in zip(button_texts, button_functions):
    button = QPushButton(text, main_window)  # Create button
    button.clicked.connect(function)  # Connect to the appropriate function
    layout.addWidget(button)  # Add to the layout
# Show the welcome screen first
welcome_screen = WelcomeScreen()  # Create and display the welcome screen
welcome_screen.show()
# Start the event loop
sys.exit(app.exec_())  # Start the event loop