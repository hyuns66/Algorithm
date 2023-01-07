import sys
from collections import deque

N = int(sys.stdin.readline())
tree = [list() for i in range(N)]
data = list(map(int, sys.stdin.readline().split()))
root, cnt = 0, 0
q = deque()

# 트리 생성
for i in range(N):
    idx = i
    parent = data[i]
    if parent == -1:
        root = idx
        continue
    tree[parent].append(idx)

q.append(root)
d_node = int(sys.stdin.readline())

while q:
    current = q.popleft()
    if current == d_node:
        continue
    if not tree[current]:
        cnt += 1
        continue
    else:
        if tree[current] == [d_node]:
            cnt += 1
            continue
        while tree[current]:
            child = tree[current].pop()
            q.append(child)

print(cnt)