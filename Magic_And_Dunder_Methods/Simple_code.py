#Python code
class Employee:
    def __init__(self,Name:str,salary:int):
        self.Name = Name 
        self.salary = salary
    def __str__(self):
        return 'Name = {} Salary = {}'.format(self.Name,self.salary)

emp = Employee('Ali',15000)
print(emp)