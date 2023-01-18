import sys

n, k = map(int, sys.stdin.readline().split())
history = [[0 for j in range(n+1)] for i in range(n+1)]

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    history[a][b] = 1
    history[b][a] = -1

for i in range(1, n+1):
    for j in range(1, n+1):
        for l in range(1, n+1):
            if history[j][i] == 1 and history[i][l] == 1:
                history[j][l] = 1
                history[l][j] = -1

s = int(sys.stdin.readline().rstrip())
query = []
for i in range(s):
    a, b = map(int, sys.stdin.readline().split())
    query.append((a, b))

for a, b in query:
    if history[a][b] == 0:
        print(0)
    elif history[a][b] == 1:
        print(-1)
    elif history[b][a] == 1:
        print(1)
