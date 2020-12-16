# str1 = 'yeshowmuchiloveyoumydearmotherreallyicannotbelieveit'
# str2 = 'yeaphowmuchiloveyoumydearmother'

str1 = 'abcdefa'
str2 ='bdefc'

# firstIndex = 0
lastIndex = len(str2) - 1
count = len(str1) - lastIndex

def findStr():

	# for j in range(len(str2)):
	# 	count = len(str1) - len(str2)
	# 	cnt = 0
	# 	for i in range(count):
	# 		if str2[i] in str1[j]:
	# 			print(str2[i])
	# 			cnt += 1
	# 		else:
	# 			i = j
	i = 0
	j = 0
	cnt = 0
	startFlag = 0
	endFlag = 0
	list =[]
	for j in range(len(str2)-j):
		r = j
		for i in range(len(str1)-1):
			if str1[i] == str2[j]:
				print(str2[j])
				if str1[i-1] != str2[j-1]:
					startFlag = j
				i += 1
				j += 1
				cnt += 1
			else:
				endFlag = j-1
				j = r
				cnt = 0
		# endFlag = len(str2)-1
		if startFlag > endFlag:
			list.append(str2[startFlag])
		else:
			list.append(str2[startFlag:endFlag])
	print(list)


findStr()

