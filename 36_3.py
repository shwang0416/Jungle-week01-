# 백준 10971 [외판원 순회2]
# 참고했던 레퍼런스들이 다 조금씩 백준 문제의 조건과 달랐고, 고치다보니 수습 불가능해졌다;
# 도저히 안돼서 파이썬으로 구현된 외판원문제를 다시 찾았다.
# https://jjangsungwon.tistory.com/4


import sys

def dfs(start, next, value, visited):
    global min

    if len(visited) == N:
        if travel[next][start] != 0:
            min = min if min < value + travel[next][start] else value + travel[next][start]
        return

    for i in range(N):
        if travel[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, value + travel[next][i], visited)
            visited.pop()

# N = int(input())
# travel = [list(map(int, input().split())) for _ in range(N)]

N = 4
travel = [[0, 10, 15, 20],[5, 0, 9, 10],[6, 13, 0, 12],[8, 8, 9, 0]]

min = sys.maxsize

# 각 번호에서 시작
for i in range(N):
    dfs(i, i, 0, [i])

print(min)
