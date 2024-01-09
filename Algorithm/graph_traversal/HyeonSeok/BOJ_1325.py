import sys
from collections import deque

# BFS 알고리즘
def BFS(node):
    global graph, N, m
    q = deque()
    cnt = 1
    visited = [False] * (N+1)
    q.append(node)
    visited[node] = True
    while q:
        cur = q.popleft()
        for n in graph[cur]:
            if not visited[n]:
                visited[n] = True
                q.append(n)
                cnt += 1
    return cnt


N, M = map(int, sys.stdin.readline().split())
graph = [list() for i in range(N+1)]
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    graph[b].append(a)

m = 0
answer = list()
for node in range(1, N+1):   # 모든 노드에 대하여 BFS 수행 후 answer 업데이트
    temp = BFS(node)
    if m < temp:
        answer = [node]
        m = temp
    elif m == temp:
        answer.append(node)
    else:
        continue

print(*answer)

