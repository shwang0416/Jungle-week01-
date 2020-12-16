# 백준 1914 하노이의 탑
# https://shoark7.github.io/programming/algorithm/tower-of-hanoi
# => 하노이의 탑 잘 된 설명
# https://ko.khanacademy.org/computing/computer-science/algorithms/towers-of-hanoi/e/move-three-disks-in-towers-of-hanoi
# => 하노이의 탑 직접 해보기

# <하노이의 탑 문제 속 재귀 원리>

# 3층짜리 탑을 옮기려면,
#  1) 먼저 2층까지의 탑을 나머지 기둥에 옮긴다
#  2) 맨 아래 3층을 목표 기둥에 옮긴다
#  3) 나머지 기둥에 있던 2층 탑을 목표 기둥으로 옮긴다
#  즉 3층탑 옮기기 == 2층탑 옮기기(나머지에) + 3층단 옮기기(1회) + 2층탑 다시 옮기기 (=> 3 + 1 + 3 = 7회)
#  =  2층탑 옮기기 == 1층탑(단) 옮기기(나머지에) + 2층단 옮기기(1회) + 1층탑(단) 다시 옮기기 (=> 1 + 1 + 1 = 3회)
#  =  1층탑(단) 옮기기 (=> 1회)


# 목표 N층탑의 N이 홀수일 경우 첫번째 두는 탑을 목표기둥에 옮기고, 짝수일 경우 나머지기둥에 옮긴다
# 맨 마지막 N번째 층을 목표기둥에 옮기려면 나머지탑(N-1개)이 모두 나머지기둥에 쌓여있어야 한다.
#
n = int(input())

def hanoiCount(n):

	if n == 1:
		return 1
	return hanoiCount(n-1)*2 + 1

def hanoi(n,start, end, left):

	if n == 1:
		print(start, end)
		return

	hanoi(n-1, start, left, end)
	# n-1개를 출발지(start)에서 경유지(left)로 옮긴다.

	print(start, end)
	# 출발지에 남아있던 맨 밑단을 목적지로 옮긴다. (출력)

	hanoi(n-1, left, end, start)
	# n-1개를 경유지(left)에서 목적지(end)로 옮긴다.

print(hanoiCount(n))
if(n <= 20):
	hanoi(n,'1','3','2');


