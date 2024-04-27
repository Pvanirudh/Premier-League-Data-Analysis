import sys
import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore

# Define the GUI class
class PremierLeagueAnalysis(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # Load the data
        self.df = pd.read_csv('epl_results_2022-23.csv')
        self.df['Date'] = pd.to_datetime(self.df['Date'], format='%d/%m/%Y')
        self.df['Week'] = self.df['Date'].dt.isocalendar().week
        # GUI layout
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        # Header
        self.lbl_title = QtWidgets.QLabel("Premier League Weekly Analysis")
        self.lbl_title.setFont(QtGui.QFont("Arial", 18))  # Corrected import for QtGui
        self.layout.addWidget(self.lbl_title)
        # Week selection
        self.cb_week = QtWidgets.QComboBox()
        self.cb_week.addItems(map(str, sorted(self.df['Week'].unique())))
        self.cb_week.setCurrentIndex(0)
        self.cb_week.currentIndexChanged.connect(self.update_table)
        self.layout.addWidget(self.cb_week)
        # Data table
        self.table = QtWidgets.QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Home Team", "Home Goals", "Away Team", "Away Goals"])
        self.layout.addWidget(self.table)
        self.update_table()  # Initial load
    def update_table(self):
        # Get the selected week
        selected_week = int(self.cb_week.currentText())
        # Filter the data by the selected week
        weekly_data = self.df[self.df['Week'] == selected_week]
        # Update the table with the filtered data
        self.table.setRowCount(len(weekly_data))
        for idx, row in enumerate(weekly_data[['HomeTeam', 'FTHG', 'AwayTeam', 'FTAG']].values):
            for col, item in enumerate(row):
                self.table.setItem(idx, col, QtWidgets.QTableWidgetItem(str(item)))
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    analysis = PremierLeagueAnalysis()
    analysis.show()
    sys.exit(app.exec_())