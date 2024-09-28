def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    root = a if a>b else b
    for key, value in parent.items():
        if value == a or value == b:
            parent[key] = root

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return a

idx = 1
while True:
    N = int(input())
    if N == 0:
        break
    parent = dict()
    for _ in range(N):
        a, b = input().split()
        if a not in parent.keys():
            parent[a] = a
        if b not in parent.keys():
            parent[b] = b
        union(parent, parent[a], parent[b])
    answer = set(parent.values())
    print(idx, len(answer))
    idx += 1