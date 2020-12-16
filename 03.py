num1 = int(input())
num2 = int(input())

hundred = int(num2 / 100)
ten = int((num2 - hundred*100)/10)
one = num2 - hundred*100 - ten*10

oneR = one * num1
tenR = ten * num1
hundredR = hundred * num1

result = oneR + tenR*10 + hundredR*100

print(oneR)
print(tenR)
print(hundredR)
print(result)
