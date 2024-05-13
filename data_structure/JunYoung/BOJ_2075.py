# N번째 큰 수

import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    for val in line:
        if len(heap) == N:
            heapq.heappushpop(heap, val)
        else:
            heapq.heappush(heap, val)

print(heapq.heappop(heap))