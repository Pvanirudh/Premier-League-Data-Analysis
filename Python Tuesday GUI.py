import sys
import subprocess
import pandas as pd
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QMainWindow,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

# Global list to hold references to open windows
open_windows = []
# Function to set the background image for a widget
def set_background(widget, image_path):
    background_label = QLabel(widget)
    background_label.setPixmap(QPixmap(image_path).scaled(1920, 1080, Qt.IgnoreAspectRatio))
    background_label.setGeometry(0, 0, 1920, 1080)
    background_label.lower()
# Define the NewWindow class for general windows
class NewWindow(QMainWindow):
    def __init__(self, title, background_image_path):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 1920, 1080)  # Set geometry for 1920x1080 resolution
        set_background(self, background_image_path)
        self.initUI(title)
    def initUI(self, title):
        self.label = QLabel("This is the content for: " + title, self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(710, 490, 500, 100)  # Centered within 1920x1080
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.back_button.clicked.connect(self.close)
        self.back_button.setGeometry(10, 10, 60, 30)
        self.back_button.setStyleSheet("QPushButton { color: white; background-color: #333; }")
# Define the CSVDataDisplayApp class for displaying CSV data with a dropdown
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
        self.dropdown.addItems(self.data['Squad'].unique())  # Populate with unique team names
        self.dropdown.currentIndexChanged.connect(self.update_table)  # Connect to the update function
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
        # Add a back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.back_button.clicked.connect(self.close)
        self.back_button.setGeometry(10, 1000, 60, 30)
        self.back_button.setStyleSheet("QPushButton { color: white; background-color: #333; }")
    def update_table(self):
        # Get the selected team name from the dropdown
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
        self.table.setSortingEnabled(True)  # Allow sorting by column
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Stretch columns to fill space
        self.table.verticalHeader().setDefaultSectionSize(30)  # Adjust row height
      
        self.table.setStyleSheet("alternate-background-color: #F0F0F0; background-color: #fff;")
# Define the new function to create a window that runs a different Python file
class ExternalScriptWindow(QMainWindow):
    def __init__(self, script_path):
        super().__init__()
        self.setWindowTitle("Player Passing Type (Script Output)")
        self.setGeometry(100, 100, 800, 600)  # Standard window size
        self.run_script(script_path)
    def run_script(self, script_path):
        # Run the external Python script and capture its output
        output = subprocess.run(["python", "passing.py" ], capture_output=True, text=True)
        # Display the output in a QLabel
        label = QLabel(output.stdout, self)
        label.setAlignment(Qt.AlignTop)  # Align text to the top
        self.setCentralWidget(label)
        # Add a back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setFont(QFont("Arial", 10, QFont.Bold))
        self.back_button.clicked.connect(self.close)
        self.back_button.setGeometry(10, 10, 60, 30)
        self.back_button.setStyleSheet("QPushButton { color: white; background-color: #333; }")
        
# Function to create the new window when the button is clicked
def create_player_passing_type_script_window():
    script_window = ExternalScriptWindow("passing.py")  # Change this to your script's path
    script_window.show()
    open_windows.append(script_window)
# Functions to create specific windows
def create_season_stats_window():
    plot_window = PlotWindow_tackle_stat()
    plot_window.show()
    open_windows.append(plot_window)
def create_team_stats_window():
    csv_window = CSVDataDisplayApp()
    csv_window.show()
    open_windows.append(csv_window)
def create_player_passing_type_window():
    new_window = NewWindow("Player Passing Type", "path_to_player_comparison_background.jpg")
    new_window.show()
    open_windows.append(new_window)
def create_standings_weekly_window():
    new_window = NewWindow("Weekly Standings", "path_to_standings_weekly_background.jpg")
    new_window.show()
    open_windows.append(new_window)
def create_team_info_window():
    new_window = NewWindow("Team Info", "path_to_team_info_background.jpg")
    new_window.show()
    open_windows.append(new_window)
# Main dashboard setup
main_window = QWidget()
main_window.setWindowTitle("Premier League Dashboard")
set_background(main_window, "path_to_home_background.jpg")  # Set background for the home screen
layout = QVBoxLayout(main_window)
# List of buttons and their respective functions
button_texts = ["Season Stats", "Team Stats", "Player Passing Type (Script)", "Weekly Standings", "Team Info"]
button_functions = [
    create_season_stats_window,
    create_team_stats_window,
    create_player_passing_type_script_window,  # New button for the script
    create_standings_weekly_window,
    create_team_info_window,
]
# Add buttons to the main dashboard
for text, function in zip(button_texts, button_functions):
    button = QPushButton(text, main_window)
    button.setFont(QFont("Arial", 10, QFont.Bold))
    button.setStyleSheet(
        """
        QPushButton {
            color: white;
            background-color: #0053A0;
            border-radius: 8px;
            padding: 8px 12px;
        }
        QPushButton:hover {
            background-color: #0066CC;
        }
        """
    )
    button.clicked.connect(function)
    layout.addWidget(button)
main_window.setLayout(layout)
# Welcome screen class
class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1920, 1080)  # Set geometry for 1920x1080 resolution
        set_background(self, "premier league gif.gif")  # Set animated background
        self.setupUI()
    def setupUI(self):
        start_button = QPushButton("Click to Start", self)
        start_button.setFont(QFont("Arial", 12, QFont.Bold))
        start_button.setGeometry(860, 800, 200, 50)  # Position in the middle
        start_button.setStyleSheet(
            """
            QPushButton {
                color: white;
                background-color: #0053A0;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #0066CC;
            }
            """
        )
        start_button.clicked.connect(self.open_dashboard)
    def open_dashboard(self):
        self.close()  # Close the welcome screen
        main_window.show()  # Show the main dashboard
# Initialize the application
app = QApplication(sys.argv)
# Show the welcome screen first
welcome_screen = WelcomeScreen()
welcome_screen.show()
# Start the event loop
sys.exit(app.exec_())