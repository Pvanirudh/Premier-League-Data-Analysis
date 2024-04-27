import sys
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QComboBox, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
# Load the CSV data
file_path = "player_premier_league_passing.csv"
df = pd.read_csv(file_path)
# Create the display names for the dropdown (player name and squad)
df['Display'] = df['Player'] + ' - ' + df['Squad']  # Concatenate player name and squad
# The attributes to be included in the pie chart
pie_chart_attributes = ['LongPasses_Comp', 'MedPasses_Comp', 'ShortPasses_Comp']
# Class for the pie chart with adjustments to avoid overlapping
class PieChartWidget(FigureCanvas):
    def __init__(self, player_data):
        # Create a larger figure to accommodate a bigger pie chart
        self.fig = Figure(figsize=(10, 8))  # Larger figure size
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
        # Adjusted pie chart data
        labels = pie_chart_attributes
        data = player_data[labels].astype(float)  # Corresponding values
        # Adjustments to avoid overlapping labels
        label_distance = 0.5  # Increased distance between labels and pie chart
        label_angle = 0  # Keep rotation at 0 for clear text
        # Separate the slices to avoid overlapping labels and percentages
        explode = [0, 0, 0]  # Separate each slice slightly
        # Create a pie chart with title at the top
        self.ax.pie(
            data,
            labels=labels,
            autopct='%1.1f%%',  # Percentage format
            startangle=90,  # Aligns the start to avoid crowding
            textprops={'rotation': label_angle, 'fontweight': 'bold', 'va': 'bottom'},  # Percentage on top
            pctdistance=label_distance,  # Distance between percentage labels and pie chart
            explode=explode,  # Adds separation between slices
        )
        # Title at the top of the pie chart
        self.ax.set_title("Player Passing Metrics ", fontweight= 'bold', pad=10)
# Main GUI class with adjusted window size and heading position
class MainApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Create a layout
        layout = QVBoxLayout()
        # Create a dropdown with player names and their team names
        self.combo = QComboBox()
        self.combo.addItems(df['Display'])  # Add the combined player name and squad
        layout.addWidget(self.combo)
        # Create a label to display the pie chart
        self.chart_label = QLabel()
        layout.addWidget(self.chart_label)
        # Connect the dropdown selection change to the pie chart update
        self.combo.currentIndexChanged.connect(self.update_chart)
        # Set layout and window size
        self.setLayout(layout)
        self.setGeometry(100, 100, 1080, 960)  # Set window size to 1080 x 960
    def update_chart(self, index):
        # Extract the original player name from the combined text
        display_text = self.combo.currentText()
        player_name = display_text.split(' - ')[0]  # Get the player name
        player_data = df[df['Player'] == player_name].iloc[0]  # Get data for the selected player
        # Create a new PieChartWidget with the adjusted size and percentage on top
        self.chart = PieChartWidget(player_data)
        self.chart_label.setPixmap(self.chart.grab())
# Run the application
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())