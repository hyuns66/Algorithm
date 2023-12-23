# 트리의 부모 찾기

import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [set() for i in range(N)]

for i in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    graph[A - 1].add(B)
    graph[B - 1].add(A)

visited = [0 for i in range(N)] # 0: 방문안함 / 0이 아닌 숫자: 루트번호
queue = deque([1])

while queue:
    n = queue.popleft()
    for adj in graph[n - 1]:
        if visited[adj - 1] == 0:
            visited[adj - 1] = n
            queue.append(adj)


for i in range(1, len(visited)):
    print(visited[i])
