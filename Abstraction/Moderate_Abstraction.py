# Moderate Abstarction Code
from abc import ABC,abstractmethod

class Living_Being(ABC): #Can't Create the object of this Parent Class.
	@abstractmethod
	def Movement(self):
		pass
class Human(Living_Being):
	def Movement(self):
		return 'Can Walk, Run, Eat and Make Things.'
class Animal(Living_Being):
	def Movement(self):
		return 'Can Walk, Run and Eat.'
class Bird(Living_Being):
	def Movement(self):
		return 'Can Fly and Eat.'
#creating Objects

Human = Human()
Animal = Animal()
Bird = Bird()

#Calling Methods
print(Human.Movement())
print(Animal.Movement())
print(Bird.Movement())