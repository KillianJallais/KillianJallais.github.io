from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class MenuFrame(QWidget):

	def __init__(self):
		super().__init__()

		self.initFrame()

	def initFrame(self):
		self.mainGrid = QVBoxLayout()
		self.setLayout(self.mainGrid)

		self.addButton = QPushButton("Ajouter un Timer")
		self.addButton.setStyleSheet("QPushButton {font-size: 20pt; padding: 10 20 10 20;}")
		self.mainGrid.addWidget(self.addButton, stretch=1, alignment=Qt.AlignCenter)

		self.loadButton = QPushButton("Démarrer un Timer")
		self.loadButton.setStyleSheet("QPushButton {font-size: 20pt; padding: 10 20 10 20;}")
		self.mainGrid.addWidget(self.loadButton, stretch=1, alignment=Qt.AlignCenter)