import sys
import heapq

N = int(sys.stdin.readline())

heap = list()
dataset = list()

for i in range(N):
    dataset = map(int, sys.stdin.readline().split())
    for data in dataset:
        if len(heap) < N:
            heapq.heappush(heap, data)
        else:
            min_num = heapq.heappop(heap)
            min_num = max(min_num, data)
            heapq.heappush(heap, min_num)

print(heapq.heappop(heap))