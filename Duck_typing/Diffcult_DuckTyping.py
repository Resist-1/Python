# Python Code

# If it looks like a duck and quacks like a duck, it’s a duck
class Car:
	def Details(self):
		print('BMW is Here.')

class Bike:
	def Details(self):
		print('Honda 125 is Here')

class Aeroplane:
	def Details(self):
		print('Im an Military Aeroplane.')
	def Name(self):
		print('Im an Military Aeroplane.')

try:
	for obj in Car(),Bike(),Aeroplane():
		obj.Name()
except AttributeError:
	print('Name() Method Does not Found.')
finally:
	print('OK...')

# In this example we counter the Error. And if you want
# to print Details() and replace the Name() in TRY block.