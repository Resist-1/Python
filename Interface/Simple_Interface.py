from abc import ABC, abstractmethod

class NetworkInterface(ABC):
  @abstractmethod
  def connect(self):
    pass
  @abstractmethod
  def transfer(self):
    pass

class RealNetwork(NetworkInterface):
  def connect(self):
    return 'Connected to Network'
  def transfer(self):
    return 'Sending Data ...'

class FakeNetwork(NetworkInterface):
  def connect(self):
    return 'Intrusion Seccessfully'
  def transfer(self):
    return 'Data is being Intercepting ...'

for N in RealNetwork(),FakeNetwork():
  print(N.connect())
  print(N.transfer())