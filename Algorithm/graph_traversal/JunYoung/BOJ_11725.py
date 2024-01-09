# 트리의 부모 찾기

import sys
from collections import deque

N = int(sys.stdin.readline())

node = [set() for i in range(N)]

for i in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    node[A - 1].add(B)
    node[B - 1].add(A)

visited = [0 for i in range(N)]
root = [0 for i in range(N)]
queue = deque()
queue.append(1)

while queue:
    n = queue.popleft()
    if visited[n-1] == 0: # not visited
        visited[n-1] = 1
        for m in node[n-1]:
            if visited[m-1] == 0:
                root[m-1] = n
                queue.append(m)

# print(root)

for i in range(1, len(root)):
    print(root[i])

# dfs로 푸니까 런타임 에러 (RecursionError) :  재귀 호출의 최대 깊이를 초과
# bfs로 바꾸고, 재귀-재귀 안하게 바꿔서 해결함
