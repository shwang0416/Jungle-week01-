str1 = 'yeshowmuchiloveyoumydearmotherreallyicannotbelieveit'
str2 = 'yeaphowmuchiloveyoumydearmother'

list1 =[]
list2 =[]

for i in range(0,len(str1)):
	list1.append(str1[i:i+1])
for i in range(0,len(str2)):
	list2.append(str2[i:i+1])

firstIndex = 0
lastIndex = len(str2) - 1
count = len(str1) - lastIndex

index = -1
# flag = 0

# lastIndex - firstIndex


for i in range(0,count):    # count번 찾음
	for j in range(0,int(lastIndex/2)):		#
		if list1[i+j] == list2[firstIndex+j] and list1[i+lastIndex-j] == list2[lastIndex-j]:
			print(str(i+j) + ' '+ str(firstIndex+i) + ' ' + str(i+lastIndex-j)+ ' '+ str(lastIndex-j))
			if(i == count-1):
				flag = 1
				index = i
			j += 1
		else:
			break
		# if flag == 1:
		# 	break
	# i += 1

print(index)
