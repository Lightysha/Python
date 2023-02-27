import math

a = int(input("Введи 1 число:"))
b = int(input("Введи 2 число:"))
n =1
z1 = (math.sin(a)+math.cos(2*b-a))/(math.cos(a)-math.sin(2*b-a))
print("ответ:", z1)

z2 = (math.sqrt(a)-math.sqrt(b))/(a)
print("ответ:", z2)