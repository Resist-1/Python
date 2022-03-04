#Python Code

class mixin_class(object):
    def __ne__(self, val) -> int:
        return not (self == val)
    def __lt__(self, val) -> int:
        return self <= val and (self != val)
    def __gt__(self, val) -> int:
        return not self <= val
    def __ge__(self, val) -> int:
        return self == val or self > val

class num_class(mixin_class):
    def __init__(self, i) -> int:
        self.i = i
    def __le__(self, val) -> int:
        return self.i <= val.i
    def __eq__(self, val) -> int:
        return self.i == val.i

print(num_class(10) <  num_class(51))
print(num_class(3) != num_class(2))
print(num_class(5) >  num_class(2))
print(num_class(5) >= num_class(3))