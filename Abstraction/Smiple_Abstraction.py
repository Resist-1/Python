# Smiple Abstraction Code
from abc import ABC

class Car(ABC):
	#Abstract Method
	def Engine(self):
		pass
class Honda(Car):
	def Engine(self):
		print('Top End Car.')
class Suzuki(Car):
	def Engine(self):
		print('Mid Range Car.')
class Mehran(Car):
	def Engine(self):
		print('Low End Car.')

#creating Objects
drive_Honda = Honda()
drive_Suzuki = Suzuki()
drive_Mehtan = Mehran()

#Calling Methods
drive_Honda.Engine()
drive_Suzuki.Engine()
drive_Mehtan.Engine()