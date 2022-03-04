class Student:  
    def __init__(self,name,grade):  
         self.name = name  
         self.grade = grade  
    @property  
    def display(self):  
         return '{} got grade {}'.format(self.name,self.grade)  
  
stu = Student("Ali","B")  
print("Name:", stu.name)  
print("Grade:", stu.grade)  
print(stu.display)