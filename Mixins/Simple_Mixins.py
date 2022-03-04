#Python Code

class parent(object):
    def fun(self):
        print("fun() parent")

class mixin_1(object):
    def fun(self):
        print("fun() mixin 1")

class mixin_2(object):
    def fun(self):
        print("fun() mixin 2")

class child(mixin_2, mixin_1, parent):
    pass

ob = child()
ob.fun()