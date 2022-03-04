# Composition Python Code

class Salary:
	def __init__(self,pay,bonus):
		self._pay = pay
		self._bonus = bonus
	def annual_salary(self):
		return (self._pay*12) + self._bonus

class Employee:
	def __init__(self,name,age,pay,bonus):
		self.name = name
		self.age = age
		self.Salary = Salary(pay,bonus)
	def total_salary(self):
		return '{} your Aunnal Salary is {}'.format(self.name,self.Salary.annual_salary())

Empy = Employee('Haider',21,25000,10000)
print(Empy.total_salary())