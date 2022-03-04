# Composition Python Code

class School():
	def __init__(self,first_name,last_name,semester):
		self.first_name = first_name
		self.last_name = last_name
		self.semester = semester

class Student():
	def __init__(self):
		self.School = School('Haider','Ittefaq','5') #Compositon
	def Details(self):
		return '{} is in {} Semester.'.format(self.School.first_name+' '+self.School.last_name,self.School.semester)

std = Student()

print(std.Details())