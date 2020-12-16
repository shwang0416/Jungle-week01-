# 백준 1181 [단어 정렬]
import sys
sys.stdin = open('text/test.txt', 'r')
testcase = int(input())
a = []
wordlen =[]
for i in range(testcase):
	tmp = input()
	lentmp = len(tmp)
	if tmp not in a:
		a.append(tmp)
	if lentmp not in wordlen:
		wordlen.append(lentmp)

testcase = len(a)
wordlen.sort()
for wlen in wordlen:
	temp = []
	for i in range(testcase):
		if len(a[i]) == wlen:
			temp.append(a[i])

	if len(temp) == 0:
		continue
	elif len(temp) == 1:
		print(temp[0])
	else:
		l = len(temp)
		for i in range(l):
			temp[i] = list(temp[i])
		for ii in range(len(temp)):			#기준단어 인덱스(이 앞으로는 이미 정렬된 것)
			smallest= ii
			for m in range(ii+1,len(temp)):    #비교 단어 인덱스
				for k in range(wlen):    #기준 단어 => 글자 인덱스
					if temp[smallest][k] > temp[m][k]: #왼쪽 단어가 오른쪽 단어보다 크다면 => m으로 가야함
						smallest = m
						break
					elif temp[smallest][k] < temp[m][k]:
						break
				if m == len(temp)-1:  # 다 돌아봤다면 smallest swap
					temp[smallest], temp[ii] = temp[ii], temp[smallest]

		for i in range(l):
			print(''.join(temp[i]))
