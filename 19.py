# 백준 2908 [상수]

# 두 수를 뒤집어서 비교한 뒤 큰 수를 출력한다.

num1, num2 = input().split()

len = len(num1)

list1 = []
list2 = []
for i in range(0, len):
	list1.append(num1[i:i+1])
	list2.append(num2[i:i+1])

rev1 =''
rev2 =''
for i in range(0, len):
	rev1 = rev1 +list1[len-1-i]
	rev2 = rev2 +list2[len-1-i]

if int(rev1) > int(rev2):
	print(rev1)
else:
	print(rev2)


