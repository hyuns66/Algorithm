from collections import deque
import heapq

N = int(input())
build_time = [0]
require_time = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
restriction_count = [0 for _ in range(N+1)]
for idx in range(N):
    info = list(map(int, input().split()))
    build_time.append(info[0])
    for i in range(1, len(info)-1):
        graph[info[i]].append(idx+1)
    restriction_count[idx+1] = len(info) - 2

single_nodes = list()
q = deque()
for idx in range(1, N+1):
    if restriction_count[idx] == 0:
        single_nodes.append(idx)

while single_nodes:
    for s in single_nodes:
        q.append(s)
    single_nodes.clear()
    while q:
        building_idx = q.pop()
        for high_tech in graph[building_idx]:
            restriction_count[high_tech] -= 1
            require_time[high_tech] = max(require_time[high_tech], build_time[building_idx])
            if restriction_count[high_tech] == 0:
                single_nodes.append(high_tech)
                build_time[high_tech] += require_time[high_tech]

for i in range(1, N+1):
    print(build_time[i])