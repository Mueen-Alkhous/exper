# finding the binary equivalnt
num = input("Enter a floating number:")
precision = 100
# Conerting the integral part of the number
first = int(num[:num.index(".")])
print(first)
firstbin = []
while first != 0:
    remainder = first % 2
    first = first // 2
    firstbin.append(remainder)
firstsrt = ""
for i in reversed(firstbin):
    firstsrt += str(i)
# Converting the 
count = 0
secondbin = []
second = float("0."+num[num.index(".") + 1:])
print(second)
while second != 1.0:
    result = str(second * 2)
    secondbin.append(result[0])
    second = float(result)
    print(second)
    if second > 1:
        second = float("0."+result[result.index(".") + 1:])
    count += 1
    if count == precision:
      break
secondstr = ""
for i in secondbin:
    secondstr += str(i)

final = firstsrt + "." + secondstr
print(final)