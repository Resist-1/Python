# Python Code
class fun():
   def __init__(self,First_Name,Last_Name) -> str:
      self.First_Name = First_Name
      self.Last_Name = Last_Name
   def Email(self) -> str:
      return '{}.{}@company.com'.format(self.First_Name.lower(),self.Last_Name.lower())

f = fun('Haider','Ittefaq')
try:
   isinstance(f.details()) # Since this method is not is class fun()
   print(f.details())      # it will run the Except block.
except AttributeError:
   print(AttributeError,'"Error" Method Not Found Check Please check Method Name')