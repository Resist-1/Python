# Python Code MRO

class Grand_Father():
	def __init__(self,Name):
		self.Name = Name
	def Details(self):
		return 'Grand Father Name is {}.'.format(self.Name)
class Father(Grand_Father):
	def Details(self):
		return 'The Name of your Father is {}.'.format(self.Name)
class Child(Father):
	def Details(self):
		return 'Name of you Grand Father is {}.'.format(self.Name)

C = Child('Ali')
F = Father('Ali')
G = Grand_Father('Ali')

print(G.Details())
print(F.Details())
print(C.Details())