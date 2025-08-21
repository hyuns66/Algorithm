from collections import deque

def insert_deque(q, restrictions):
    for i, count in enumerate(restrictions):
        if count == 0:
            q.append(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
restrictions = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    restrictions[b-1] += 1

q = deque()
answer = list()
insert_deque(q, restrictions)
while q:
    node = q.popleft()
    answer.append(node + 1)
    for tar in graph[node]:
        restrictions[tar] -= 1
        if restrictions[tar] == 0:
            q.append(tar)

print(*answer)