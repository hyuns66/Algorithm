import sys

T = int(sys.stdin.readline())
answer = list()
for _ in range(T):
    N = int(sys.stdin.readline())
    parent = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    for _ in range(N-1):
        u, v = map(int, sys.stdin.readline().split())
        parent[v] = u
    a, b = map(int, sys.stdin.readline().split())
    while True:
        visited[a] = True
        if parent[a] == 0:
            break
        else:
            a = parent[a]
    while True:
        if visited[b] == True:
            answer.append(b)
            break
        else:
            b = parent[b]
print(*answer, sep='\n')