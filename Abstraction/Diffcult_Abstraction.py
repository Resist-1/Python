# Diffcult Abstarction Code
from abc import ABC,abstractmethod

class Number_System(ABC): #Can't Create the object of this Parent Class.
	def __init__(self,Num):
		self.Num = Num

	#Abtract Method
	@abstractmethod
	def Representation(self):
		return Num

class Hex_Decimal(Number_System):
	def Representation(self):
		super().__init__(self.Num)
		return 'Hexa-Decimal of {} Number is {}'.format(self.Num,hex(self.Num))

class Bin_Decimal(Number_System):
	def Representation(self):
		super().__init__(self.Num)
		return 'Binary of {} Number is {}'.format(self.Num,bin(self.Num))

class Oct_Decimal(Number_System):
	def Representation(self):
		super().__init__(self.Num)
		return 'Octal of {} Number is {}'.format(self.Num,oct(self.Num))

#creating Objects
Hex = Hex_Decimal(92)
Bin = Bin_Decimal(30)
Oct = Oct_Decimal(40)
#Calling Methods
print(Hex.Representation())
print(Bin.Representation())
print(Oct.Representation())