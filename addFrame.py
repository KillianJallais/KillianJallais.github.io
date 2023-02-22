from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFormLayout, QComboBox
from PyQt5.QtCore import Qt


class AddFrame(QWidget):

	def __init__(self):
		super().__init__()

		self.initFrame()


	def initFrame(self):
		self.mainGrid = QVBoxLayout()
		self.setLayout(self.mainGrid)

		self.title = QLabel("Créer un Timer")
		self.title.setStyleSheet("QLabel {font-size: 25pt;}")
		self.mainGrid.addWidget(self.title, stretch=1, alignment=Qt.AlignCenter)

		self.panel1 = QWidget()
		self.mainGrid.addWidget(self.panel1, stretch=4, alignment=Qt.AlignCenter)

		self.addButton = QPushButton("Ajouter le Timer")
		self.addButton.setStyleSheet("QPushButton {font-size: 20pt; padding: 10 20 10 20;}")
		self.mainGrid.addWidget(self.addButton, stretch=2, alignment=Qt.AlignCenter|Qt.AlignTop)

		self.cancelButton = QPushButton("Retour")
		self.cancelButton.setStyleSheet("QPushButton {font-size: 20pt;}")
		self.mainGrid.addWidget(self.cancelButton, stretch=1, alignment=Qt.AlignLeft)


		############## Création du paneau principale ####################

		self.grid1 = QFormLayout()
		self.grid1.setAlignment(Qt.AlignCenter)
		self.grid1.setSpacing(20)
		self.panel1.setLayout(self.grid1)

		self.nbrExLabel = QLabel("Nombre de sessions de travail :")
		self.nbrExLabel.setStyleSheet("QLabel {font-size: 15pt;}")
		self.nbrExCombo = QComboBox()
		self.nbrExCombo.setStyleSheet("QComboBox {font-size: 15pt;}")

		self.tempExLabel = QLabel("Temps d'une sessions de travail (en min) :")
		self.tempExLabel.setStyleSheet("QLabel {font-size: 15pt;}")
		self.tempExCombo = QComboBox()
		self.tempExCombo.setStyleSheet("QComboBox {font-size: 15pt;}")

		self.tempPauseLabel = QLabel("Temps d'une pause (en min) :")
		self.tempPauseLabel.setStyleSheet("QLabel {font-size: 15pt;}")
		self.tempPauseCombo = QComboBox()
		self.tempPauseCombo.setStyleSheet("QComboBox {font-size: 15pt;}")

		for i in range(100):
			self.nbrExCombo.addItem(str(i+1))
			self.tempExCombo.addItem(str(i+1))
			self.tempPauseCombo.addItem(str(i+1))

		self.grid1.addRow(self.nbrExLabel, self.nbrExCombo)
		self.grid1.addRow(self.tempExLabel, self.tempExCombo)
		self.grid1.addRow(self.tempPauseLabel, self.tempPauseCombo)

	def getInformations(self) -> tuple:
		return int(self.nbrExCombo.currentText()), int(self.tempExCombo.currentText()), int(self.tempPauseCombo.currentText())

