def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

N = int(input())
M = int(input())
cost = list()
for _ in range(M):
    a, b, c = map(int, input().split())
    cost.append((c, (a-1, b-1)))
cost.sort()
parent = [i for i in range(N)]
answer = 0
for c, (a, b) in cost:
    if a == b:
        continue
    if find(parent, a) == find(parent, b):
        continue
    union(parent, a, b)
    answer += c
print(answer)
