import math

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x > y:
        for idx, p in enumerate(parent):
            if p == x:
                parent[idx] = y
    else:
        for idx, p in enumerate(parent):
            if p == y:
                parent[idx] = x

N = int(input())
stars = list()
for _ in range(N):
    stars.append(list(map(float, input().split())))
edges = list()
for i in range(N):
    for j in range(i+1, N):
        dist = math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)
        edges.append((dist, i, j))
edges.sort()
parent = [i for i in range(N)]
answer = 0
for dist, y, x in edges:
    if parent[y] != parent[x]:
        answer += dist
        union(parent, y, x)
print("{:.2f}".format(answer, 2))