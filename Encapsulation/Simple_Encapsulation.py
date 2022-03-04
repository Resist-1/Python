# Encapsulation Python Code

class Account():
	def __init__(self,Payment):
		self._Payment = Payment # Protected Attribute
		self._Bouns = 5000		# // // // // // //
	def Bouns(self):
		return 'Payment is {}.Rs and Bouns is {}.Rs'.format(self._Payment,self._Payment+self._Bouns)

pay = Account(20000)

print(pay.Bouns())