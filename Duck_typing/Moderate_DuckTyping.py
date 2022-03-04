# Python Code

# If it looks like a duck and quacks like a duck, it’s a duck
class Car:
	def Details(self):
		print('BMW is Here.')

class Bike:
	def Details(self):
		print('Honda 125 is Here')
"""
class Aeroplane:
	def Name(self):
		print('Im an Military Aeroplane.')
	# def Details(self):
	#	print('Im an Military Aeroplane.')
"""
#If you Un-Comment the above class and add Aeroplane() in loop below
#because the Aeroplane has no method name Details.
# Or if you just Un-Comment the Details() method in Aeroplane class.
# Otherwise you will get and AttributeError.

for obj in Car(),Bike():
	obj.Details()