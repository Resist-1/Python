# Python Code
def fun(a):
   if a < 4:
   # throws ZeroDivisionError for a = 3
      b = a/(a-3)
   # throws NameError if a >= 4
   print("Value of b = ", b)
i = 0     
try:
   while(i < 5): 
      fun(i)
      i += 1 
except ZeroDivisionError:
   print("ZeroDivisionError Occurred and Handled")
except NameError:
   print("NameError Occurred and Handled")