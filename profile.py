from timer import RepetedTimer

class Profile:
	TRAVAIL = "t"
	PAUSE = "p"

	def __init__(self, nbrExercice: int, tempExercice: int, tempPause: int, *fonctions):
		self.nbrExercice = nbrExercice

		self.tempExercice = tempExercice * 60 #donné en minute mais convertie en seconde
		self.tempPause = tempPause * 60 #donné en minute mais convertie en seconde

		self.timer = None

		self.fonctions = fonctions

		self.nbrTimers = self.nbrExercice*2 - 1

		self.initProfile()

	def initProfile(self) -> None:
		self.timer = RepetedTimer(self.tempExercice, Profile.TRAVAIL, self.fonctions)
		temp = self.timer

		for i in range(1, self.nbrTimers):
			if i%2 == 0:
				temp.next = RepetedTimer(self.tempExercice, Profile.TRAVAIL, self.fonctions)
			else:
				temp.next = RepetedTimer(self.tempPause, Profile.PAUSE, self.fonctions)

			temp = temp.next

	def getTimeLeft(self) -> str:
		return self.timer.getTimeLeft()

	def start(self) -> None:
		self.timer.start()

	def stop(self):
		self.timer.stop()