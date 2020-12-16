# 백준 2753 [윤년]

year = int(input())
result = -1

if int(year%400) == 0:
	result = 1
elif int(year%100) == 0:
	result = 0
elif int(year%4) == 0:
	result = 1
else:
	result = 0

print(result)
