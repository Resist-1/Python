# Moderate Python Code

class Account():
	def __init__(self,Payment):
		self._Payment = Payment #Protected Attribute
		self._Bouns = 5000		# // // // // // //

class Payment_Bouns(Account):
	def Bouns(self):
		return 'Payment is {}.Rs and Bouns is {}.Rs'.format(self._Payment,self._Payment+self._Bouns)

class Double_Payment_Bouns(Payment_Bouns):
	def Bouns(self):
		return 'Payment is {}.Rs and Double Bouns is {}.Rs'.format(self._Payment,self._Payment+self._Bouns+2000)

pay = Account(20000)
pay2 = Payment_Bouns(20000)
pay3 = Double_Payment_Bouns(20000)

print(pay2.Bouns())
print(pay3.Bouns())