from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor


class ChoiceFrame(QWidget):

	def __init__(self, profiles, setMinuteurFrame):
		super().__init__()

		self.profiles = profiles

		self.initFrame(setMinuteurFrame)


	def initFrame(self, setMinuteurFrame):
		self.mainGrid = QVBoxLayout()
		self.setLayout(self.mainGrid)

		self.title = QLabel("Choix du Timer")
		self.title.setStyleSheet("QLabel {font-size: 20pt;}")

		self.mainGrid.addWidget(self.title, stretch=1, alignment=Qt.AlignCenter)

		self.scrollArea = QScrollArea()
		self.mainGrid.addWidget(self.scrollArea, stretch=5)

		self.cancelButton = QPushButton("Retour")
		self.cancelButton.setStyleSheet("QPushButton {font-size: 20pt;}")
		self.mainGrid.addWidget(self.cancelButton, stretch=1, alignment=Qt.AlignLeft)

		self.panel1 = QWidget()
		self.grid1 = QVBoxLayout()
		self.panel1.setLayout(self.grid1)

		for profile in self.profiles:
			self.grid1.addWidget(ClickableTimer(*profile, setMinuteurFrame), stretch=1)

		self.scrollArea.setWidget(self.panel1)


class ClickableTimer(QWidget):

	def __init__(self, nbrExercice: int, tempExercice: int, tempPause: int, setMinuteurFrame):
		super().__init__()

		self.nbrExercice = nbrExercice
		self.tempExercice = tempExercice
		self.tempPause = tempPause

		self.setMinuteurFrame = setMinuteurFrame

		self.initUI()

	def initUI(self):
		self.grid = QVBoxLayout()
		self.setLayout(self.grid)

		self.setStyleSheet("QWidget {border: 1px solid black;}")
		self.setCursor(QCursor(Qt.PointingHandCursor))

		text = f"{self.nbrExercice} * sessions de travail de {self.tempExercice} minutes"
		text += "\n"
		text += f"{self.nbrExercice - 1} * pauses de {self.tempPause} minutes"

		self.label = QLabel(text)
		self.label.setStyleSheet("QLabel {font-size: 10pt;}")

		self.grid.addWidget(self.label)


	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.setMinuteurFrame(self.nbrExercice, self.tempExercice, self.tempPause)
