# DFS와 BFS

import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

nodes = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    nodes[A - 1].append(B)
    nodes[B - 1].append(A)

# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문한다.
for i in range(N):
    nodes[i] = sorted(list(set(nodes[i])))

# dfs
visited = [0 for i in range(N)]
dfsList = []


def dfs(i):
    dfsList.append(i)
    visited[i - 1] = 1
    for n in nodes[i - 1]:
        if visited[n - 1] == 0:
            dfs(n)


dfs(V)

# bfs
visited = [0 for i in range(N)]
queue = deque()
queue.append(V)

bfsList = []
while queue:
    n = queue.popleft()
    if visited[n-1] == 0:
        bfsList.append(n)
        visited[n - 1] = 1
        for m in nodes[n - 1]:  # 갈 수 있는 곳 중에서
            if visited[m - 1] == 0:
                queue.append(m)

# 결과 출력
for i in dfsList:
    print(i, end=' ')
print()
for i in bfsList:
    print(i, end=' ')

# dfs는 재귀함수로 밖에 못짜는 것일까?


# 11 4 2
# 2 1
# 2 3
# 2 11
# 2 5
