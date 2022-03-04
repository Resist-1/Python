# Python Code
from abc import ABC,abstractmethod

class Number_System(ABC): #Can't Create the object of this Parent Class.
  def __init__(self,Num) -> int:
    self.Num = Num

  #Abtract Method
  @abstractmethod
  def Representation(self) -> int:
    return Num

class Hex_Decimal(Number_System):
  def Representation(self):
    super().__init__(self.Num)
    return 'Hexa-Decimal of {} Number is {}'.format(self.Num,hex(self.Num))

class Binary(Number_System):
  def Representation(self):
    super().__init__(self.Num)
    return 'Binary of {} Number is {}'.format(self.Num,bin(self.Num))

class Octal(Number_System):
  def Representation(self):
    super().__init__(self.Num)
    return 'Octal of {} Number is {}'.format(self.Num,oct(self.Num))

#Calling Methods
for NS in Hex_Decimal(53),Binary(23),Octal(34):
  print(NS.Representation())
