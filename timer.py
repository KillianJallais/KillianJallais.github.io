from threading import Timer
import pyaudio
import wave


class RepetedTimer:
	SONNERIE = "sonnerie.wav"
	INTER = 1
	TYPES = ["t", "p"]

	def __init__(self, timeOut: int, timerType: str, fonctions):
		self.setTimeOut(timeOut)
		self.setType(timerType)

		self.updateTime = fonctions[0] #minuteurFrame
		self.updateFrame = fonctions[1] #minuteurFrame
		self.updateTitle = fonctions[2] #minuteurFrame

		self.time = 0 #compteur
		self.running = False
		self.next = None #timer suivant (RepetedTimer)

		self.timer = None

	def _run(self):  #partie qui execute les fonctions importé
		self.updateTime(self.getTimeLeft())
		self.time += 1

		self.running = False
		self.start()

	def start(self):  #démarre le RepetedTimer
		if not self.running:
			self.timer = Timer(RepetedTimer.INTER, self._run)
			self.timer.start()
			self.running = True
			self.check()

	def check(self):  #regarde si le temps est écoulé
		if self.time >= self.timeOut:
			self.stop()
			self.setNext()

	def setNext(self): #met en place le RepetedTimer suivant ou arrete tous si il n'y a pas de suivant
		if self.next:
			self.readAudio(RepetedTimer.SONNERIE)  #fait sonner l'alarme

			self = self.next
			self.start()

			self.updateTitle(self.timerType)
		else:
			self.readAudio(RepetedTimer.SONNERIE)  #fait sonner l'alarme
			self.updateFrame()			

	def stop(self): #arrête le RepetedTimer en cour
		self.timer.cancel()
		self.running = False

	def getTimeLeft(self) -> str:
		timeLeft = self.timeOut - self.time

		minute = int(timeLeft/60)
		seconde = int(timeLeft%60)

		return f"{minute:02d}:{seconde:02d}"

	def setTimeOut(self, timeOut: int):
		if timeOut < 0:
			raise ValueError(f"Limite de temps non conforme : {timeOut}")
		else:
			self.timeOut = timeOut

	def setType(self, timerType: str) -> None:
		if timerType not in RepetedTimer.TYPES:
			raise Exception(f"Le type de timer donner n'est pas valide : {timerType}")
		else:
			self.timerType = timerType

	def readAudio(self, fileName):
		chunk = 1024

		try:
			with wave.open(fileName, "rb") as file:
				p = pyaudio.PyAudio()

				stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
		                channels = file.getnchannels(),
		                rate = file.getframerate(),
		                output = True)

				data = file.readframes(chunk)

				while len(data) > 0:
				    stream.write(data)
				    data = file.readframes(chunk)

			stream.stop_stream()
			stream.close()
			p.terminate()
			
		except FileNotFoundError:
			pass

	def __repr__(self):
		return f"RepetedTimer({self.timeOut}, {self.timerType})"