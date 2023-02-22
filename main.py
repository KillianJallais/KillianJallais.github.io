import sys
import pickle
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from profile import Profile

from menuFrame import MenuFrame
from addFrame import AddFrame
from choiceFrame import ChoiceFrame
from minuteurFrame import MinuteurFrame


class Window(QMainWindow):
	TITLE = "Pomodore"

	def __init__(self, width, height, saveProfiles):
		super().__init__()

		self.width = width
		self.height = height

		self.saveProfiles = saveProfiles

		self.initUI()

	def initUI(self) -> None:
		self.setGeometry(0, 0, self.width, self.height)
		self.setWindowTitle(Window.TITLE)

		self.show()

	def setFrame(self, frame) -> None:
		self.setCentralWidget(frame)

	def closeEvent(self, event):
		self.saveProfiles()
		event.accept()


class Application:

	def __init__(self):
		self.width = 1600
		self.height = 1300

		self.profiles = []

		self.menuFrame = None
		self.addFrame = None
		self.choiceFrame = None
		self.minuteurFrame = None

		self.profile = None

		self.window = Window(self.width, self.height, self.saveProfiles)
		self.setMenuFrame()

		self.setConnections()

		self.loadProfiles()

	def loadProfiles(self):
		print("Chargement des profiles")
		try:
			with open("profile.txt", "rb") as file:
				data = pickle.load(file)
				self.profiles = data

		except FileNotFoundError:
			with open("profile.txt", "wb") as file:
				pass

	def addprofile(self):
		print("Ajout d'un profile")
		info = self.addFrame.getInformations()
		self.profiles.append(info)

		self.saveProfiles()
		self.loadProfiles()

		self.setMenuFrame()

	def saveProfiles(self):
		print("Sauvegarde des profiles")
		with open("profile.txt", "wb") as file:
			pickle.dump(self.profiles, file)

	def setMenuFrame(self):
		self.menuFrame = MenuFrame()
		self.window.setFrame(self.menuFrame)

		self.addFrame = None
		self.choiceFrame = None
		self.minuteurFrame = None

		self.setConnections()

	def setAddFrame(self):
		self.addFrame = AddFrame()
		self.window.setFrame(self.addFrame)

		self.menuFrame = None
		self.choiceFrame = None
		self.minuteurFrame = None

		self.setConnections()

	def setChoiceFrame(self):
		self.choiceFrame = ChoiceFrame(self.profiles, self.setMinuteurFrame)
		self.window.setFrame(self.choiceFrame)

		self.menuFrame = None
		self.addFrame = None
		self.minuteurFrame = None

		self.setConnections()

	def setMinuteurFrame(self, nbrExercice: int, tempExercice: int, tempPause: int):
		self.minuteurFrame = MinuteurFrame()
		self.window.setFrame(self.minuteurFrame)

		self.profile = Profile(nbrExercice, tempExercice, tempPause, self.updateTime, self.minuteurFrame.updateFrame, self.updateTitle)

		self.minuteurFrame.setTime(self.profile.getTimeLeft())

		self.profile.start()

		self.menuFrame = None
		self.addFrame = None
		self.choiceFrame = None

		self.setConnections()

	def cancelMinuteur(self):
		self.profile.stop()
		self.profile = None
		self.setMenuFrame()


	def updateTime(self, time):
		self.minuteurFrame.temp.setText(time)

	def updateTitle(self, title):
		if title == "t":
			self.minuteurFrame.title.setText("Travail")
		else:
			self.minuteurFrame.title.setText("Pause")

	def setConnections(self):
		if self.menuFrame:
			self.menuFrame.addButton.clicked.connect(self.setAddFrame)
			self.menuFrame.loadButton.clicked.connect(self.setChoiceFrame)

		if self.addFrame:
			self.addFrame.cancelButton.clicked.connect(self.setMenuFrame)
			self.addFrame.addButton.clicked.connect(self.addprofile)

		if self.choiceFrame:
			self.choiceFrame.cancelButton.clicked.connect(self.setMenuFrame)

		if self.minuteurFrame:
			self.minuteurFrame.cancelButton.clicked.connect(self.cancelMinuteur)


def main():
	app = QApplication(sys.argv)

	pomodore = Application()

	sys.exit(app.exec_())


if __name__ == "__main__":
	main()