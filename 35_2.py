# 백준 10819 [차이를 최대로] 완전탐색_중

# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 그게 최댓값이 아니었나봄...
# n = 6
# a =[20, 1, 15, 8, 4, 10]
n = int(input())
a = list(int(i) for i in input().split())

# 순열 방식으로 재도전 (perm)
# 참고: https://gorakgarak.tistory.com/522

def cal(a, n):

	# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
	result = 0
	for i in range(n-1):
		tmp = abs(a[i]-a[i+1])
		result += tmp
	return result

def swap(i, j):
	a[i], a[j] = a[j], a[i]


temp = []
def perm(a, depth, n):	# 길이가 n인 배열 a가 가질 수 있는 모든 조합 만들기(재귀를 이용한 순열 알고리즘)

	# 종료조건: depth가 n이면 조합이 하나 완성된 것이므로 return
	#   => 어차피 n-1까지만 뽑으면  마지막 숫자는 고정이므로 n => n-1로 바꿔줌

	if depth == n - 1: # 다 뽑았니?
		tmp = cal(a,n)
		temp.append(tmp)
		return

	for i in range(depth, n): #
		swap(i, depth)
		perm(a,depth+1,n)
		swap(i, depth) #한번 다 뽑은 뒤 그 전단계로 돌아와서 실행됨

perm(a, 0, n)

max = 0
for i in range(len(temp)):
	if max < temp[i]:
		max = temp[i]
print(max)
