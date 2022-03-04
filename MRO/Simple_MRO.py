# Python Code MRO

class Grand_Father():
	def Details(self,Name):
		return 'Grand Father Name is {}.'.format(Name)
class Father(Grand_Father):
	def Details(self,Name):
		return 'The Name of your Father is {}.'.format(Name)
class Child(Father):
	def Details(self,Name):
		return 'Name of you Grand Father is {}.'.format(Name)

C = Child()
F = Father()
G = Grand_Father()

print(C.Details('Ali'))
print(F.Details('Ali'))
print(G.Details('Ali'))
