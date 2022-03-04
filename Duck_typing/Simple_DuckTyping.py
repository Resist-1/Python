# Python Code

# If it looks like a duck and quacks like a duck, it’s a duck
class Car:
	def Details(self):
		print('BMW is Here.')

class Bike:
	def Details(self):
		print('Honda 125 is Here')

for obj in Car(),Bike():
	obj.Details()