# Python Code
from abc import ABC, abstractmethod
class Payment(ABC):
  @abstractmethod # Abstract Method
  def payment(self, amount):
    pass

class CreditCardPayment(Payment):
  def payment(self, amount) -> int:
    print('Credit card payment of-', amount)

class MobileWalletPayment(Payment):
  def payment(self, amount) -> int:
    print('Mobile wallet payment of-', amount)

for obj in CreditCardPayment(),MobileWalletPayment():
  obj.payment(200)

print(isinstance(obj, Payment)) # Checking Method