import sys
from collections import deque

N = int(sys.stdin.readline())
leafs = list()
nodes = [list() for j in range(N+1)]

# make tree
for i in range(N-1):
    p, c, size = map(int, sys.stdin.readline().split())
    nodes[p].append((c, size))
    nodes[c].append((p, size))

# BFS (make leafs)
q = deque()
q.append(1)
visited = [False for i in range(N+1)]
while q:
    current = q.popleft()
    toggle = False
    visited[current] = True
    for c in nodes[current]:
        if visited[c[0]]:
            continue
        q.append(c[0])
        toggle = True
    if not toggle:
        leafs.append(current)

# BFS for all leafs
answer = 0

for leaf in leafs:
    q = deque()
    visited = [False for i in range(N + 1)]
    q.append((leaf, 0))
    while q:
        current = q.popleft()
        toggle = False
        for child in nodes[current[0]]:
            if visited[child[0]]:
                continue
            q.append((child[0], current[1] + child[1]))
            toggle = True
            visited[current[0]] = True
        if not toggle and answer < current[1]:
            answer = current[1]

print(answer)