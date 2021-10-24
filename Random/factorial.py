# Calculating n! #1
n = int(input("Please, enter a number: "))
num = n
if n > 0:
    while n > 2:
        num = num * (n - 1)
        n = n - 1
    print(num)
else:
    if n == 0:
        num = 1
        print(num)
    else:
        print("Error, Connot compute negative factorials")

# Calculating n! #2
n = int(input("Please, enter a number: "))
num, i = n, 2
if n > 0:
    while i < n:
        num = num * i
        i = i + 1
    print (num)
else:
    if n == 0:
        num = 1
        print (num)
    else:
        print("Error, connot compute nagative factorials")


num = 1
n = int(input("   ---   "))
for i in range(2, n + 1):
    num = num * i
print(num)
