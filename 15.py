# 백준 15596 [정수 N개의 합]

# input = list(map(int, input().split()))
# sum = 0
# for i in input:
# 	sum = sum + i

# print(sum)

# 함수 sum(a) 구현

def solve(a):
    ans = 0
    for i in a:
	    ans = ans + i
    return ans


