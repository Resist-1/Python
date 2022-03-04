# Diffcult Python Code

class Account():
	def __init__(self,Payment):
		self._Payment = Payment #Protected Attribute
		self.__Bouns = 5000		#Private Attribute
	def Bouns(self):
		return 'Payment for Grand Parent is {}.Rs'.format(self._Payment+self.__Bouns)
 
class Payment_Bouns(Account):
	def Bouns(self):
		#print(self.__Bouns)
		#if you Un-Comment this line you will get Error
		#Even this class inheriting Account() class.
		return 'Payment for Parent is {}.Rs'.format(self._Payment+7000)

class Double_Payment_Bouns(Account):
	def Bouns(self):
		return 'Payment for Child is {}.Rs'.format(self._Payment+9000)

pay = Account(20000)
pay2 = Payment_Bouns(20000)
pay3 = Double_Payment_Bouns(20000)

print(pay.Bouns())
print(pay2.Bouns())
print(pay3.Bouns())