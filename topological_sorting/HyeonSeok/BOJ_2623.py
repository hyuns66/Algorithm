from collections import deque
        
N, M = map(int, input().split())
incount = [0 for _ in range(N+1)]
graph = [set() for _ in range(N+1)]
q = deque()
for _ in range(M):
    numbers = list(map(int, input().split()))
    for i, n in enumerate(numbers):
        if i == 0:
            continue
        if i < len(numbers)-1:
            graph[n].add(numbers[i+1])
for i, g in enumerate(graph):
    for num in g:
        incount[num] += 1

for i in range(1, N + 1):
    if incount[i] == 0:
        q.append(i)
answer = list()
while q:
    cur_node = q.popleft()
    # 사이클이 있어서 순서만들기 불가능한 경우
    for child_node in graph[cur_node]:
        incount[child_node] -= 1
        if incount[child_node] == 0:
            q.append(child_node)
    answer.append(cur_node)

if len(answer) == N:
    for a in answer:
        print(a)
else:
    print(0)