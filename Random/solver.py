# Quadratic formula solver.
import math
a = int(input("Please, Entert a: "))
b = int(input("Please, enter b: "))
c = int(input("Please, enter c: "))

delt = b**2 - 4 * a * c

if delt > 0:
    x1 = (-b + math.sqrt(delt)) / (2 * a)
    x2 = (-b - math.sqrt(delt)) / (2 * a)
    print("first root:", x1, "second root:", x2)
elif delt == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("no solution")

        
        