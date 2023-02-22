from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class MinuteurFrame(QWidget):

	def __init__(self):
		super().__init__()

		self.initFrame()

	def initFrame(self):
		self.mainGrid = QVBoxLayout()
		self.setLayout(self.mainGrid)

		self.title = QLabel("Travail")
		self.title.setStyleSheet("QLabel {font-size: 20pt;}")

		self.mainGrid.addWidget(self.title, stretch=1, alignment=Qt.AlignCenter)

		self.temp = QLabel("")
		self.temp.setStyleSheet("QLabel {font-size: 20pt;}")

		self.mainGrid.addWidget(self.temp, stretch=4, alignment=Qt.AlignCenter)

		self.cancelButton = QPushButton("Retour")
		self.cancelButton.setStyleSheet("QPushButton {font-size: 20pt;}")

		self.mainGrid.addWidget(self.cancelButton, stretch=1, alignment=Qt.AlignLeft)

	def updateFrame(self):
		self.temp.setText("Bravo, vous avez finis !")
		self.cancelButton.setText("Retour au menu")

	def setTime(self, temp):
		self.temp.setText(temp)
