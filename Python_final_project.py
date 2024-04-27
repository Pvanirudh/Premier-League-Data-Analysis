# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:18:19 2024

@author: aniru
"""

import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

open_windows = []  # List to hold references to open windows

def set_background(widget, image_path):
    background_label = QLabel(widget)
    background_label.setPixmap(QPixmap(image_path).scaled(1920, 1080, Qt.IgnoreAspectRatio))
    background_label.setGeometry(0, 0, 1920, 1080)
    background_label.lower()

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
        self.back_button = QPushButton('Back', self)
        self.back_button.setFont(QFont('Arial', 10, QFont.Bold))
        self.back_button.clicked.connect(self.close)
        self.back_button.setGeometry(10, 10, 60, 30)
        self.back_button.setStyleSheet("QPushButton { color: white; background-color: #333; }")

def create_season_stats_window():
    # Run the external Python script to generate the plot
    subprocess.run(['python', 'Test1.py'])
    
    # Load the plot image
    label = QLabel()
    pixmap = QPixmap('plot_output.png')
    label.setPixmap(pixmap)
    
    new_window = NewWindow("Season Stats", 'path_to_season_status_background.jpg')
    new_window.show()
    open_windows.append(new_window)

def create_team_stats_window():
    new_window = NewWindow("Team Stats", 'path_to_team_stats_background.jpg')
    new_window.show()
    open_windows.append(new_window)

def create_player_comparison_window():
    new_window = NewWindow("Player Comparison", 'path_to_player_comparison_background.jpg')
    new_window.show()
    open_windows.append(new_window)

def create_standings_weekly_window():
    new_window = NewWindow("Weekly Standings", 'path_to_standings_weekly_background.jpg')
    new_window.show()
    open_windows.append(new_window)

def create_team_info_window():
    new_window = NewWindow("Team Info", 'path_to_team_info_background.jpg')  # Replace with actual path
    new_window.show()
    open_windows.append(new_window)

class WelcomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 1920, 1080)  # Set geometry for 1920x1080 resolution
        set_background(self, 'premier league gif.gif')  # Set an animated background
        self.setupUI()

    def setupUI(self):
        start_button = QPushButton("Click to Start", self)
        start_button.setFont(QFont('Arial', 12, QFont.Bold))
        start_button.setGeometry(860, 800, 200, 50)
        start_button.setStyleSheet("QPushButton { color: white; background-color: #0053A0; border-radius: 10px; }")
        start_button.clicked.connect(self.open_dashboard)

    def open_dashboard(self):
        self.close()
        main_window.setGeometry(100, 100, 1920, 1080)
        main_window.show()  # Show the main window at 1920x1080

app = QApplication(sys.argv)

# Main window setup
main_window = QWidget()
main_window.setWindowTitle('Premier League Dashboard')
set_background(main_window, 'path_to_home_background.jpg')  # Set background image for home screen
layout = QVBoxLayout(main_window)

# List of buttons and their respective functions
button_texts = ["Season Stats", "Team Stats", "Player Comparison", "Weekly Standings", "Team Info"]
button_functions = [
    create_season_stats_window,
    create_team_stats_window,
    create_player_comparison_window,
    create_standings_weekly_window,
    create_team_info_window
]

for text, function in zip(button_texts, button_functions):
    button = QPushButton(text, main_window)
    button.setFont(QFont('Arial', 9, QFont.Bold))
    button.setStyleSheet("""
        QPushButton {
            color: white;
            background-color: #0053A0;
            border-radius: 8px;
            padding: 6px 10px;
            margin: 4px;
            font-size: 12px;
            font-weight: bold;
            text-align: center;
        }
        QPushButton:hover {
            background-color: #0066CC;
        }
    """)
    button.clicked.connect(function)
    layout.addWidget(button)

welcome_screen = WelcomeScreen()
welcome_screen.show()

sys.exit(app.exec_())


