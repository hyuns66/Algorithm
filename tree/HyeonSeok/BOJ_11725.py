import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
visited = [False for i in range(N+1)]
visited[1] = True
nodes = [list() for j in range(N+1)]
parents = [0 for k in range(N+1)]
queue = deque()
queue.append(1)

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

while queue:
    temp = int(queue.popleft())
    for node in nodes[temp]:
        if not visited[node]:
            parents[node] = temp
            queue.append(node)
            visited[node] = True

for i in range(1, N):
    print(parents[i+1])

# [자식, 자식]의 형태로 각 노드 인덱스에 들어감 (0번은 비워둠)
# node_set = [list() for i in range(N+1)]
# for i in range(N-1):


# for i in range(N-1):
#     indexes = list(map(int, sys.stdin.readline().split()))
#     if visited[indexes[0]]:
#         if nodes[indexes[0]-1].left is not None:
#             nodes[indexes[0]-1].right = nodes[indexes[1]-1]
#         else:
#             nodes[indexes[0]-1].left = nodes[indexes[1]-1]
#         nodes[indexes[1]-1].parent = nodes[indexes[0]-1]
#         visited[indexes[1]] = True
#     else:
#         if nodes[indexes[1]-1].left is not None:
#             nodes[indexes[1]-1].right = nodes[indexes[0]-1]
#         else:
#             nodes[indexes[1]-1].left = nodes[indexes[0]-1]
#         nodes[indexes[0]-1].parent = nodes[indexes[1]-1]
#         visited[indexes[0]] = True
#
# for i in range(1, N):
#     print(nodes[i].parent.idx)