q = input("s or z: ")
if q == "s":
    num = int(input("Enter the number of resestors: "))
    sum = 0
    for i in range(num):
        res = int(input("number"))
        sum = sum + res
else:
    num = input("Enter the number of resestors: ")
    sum = 0
    for i in range(num):
        res = input("number")
        sum = sum + res
print(sum)