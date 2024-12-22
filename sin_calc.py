import math
def SinValue(a):
  rediuns = math.radians(a)
  b= math.sin(rediuns)
  return b
x = float(input("enter a number : "))
print(SinValue(x))
