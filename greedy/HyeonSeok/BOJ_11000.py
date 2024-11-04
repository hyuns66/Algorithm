import sys
import heapq

N = int(input())
schedule = list()
inputs = list()
for _ in range(N):
    start, end = map(int, input().split())
    inputs.append((start, end))
inputs.sort()
for start, end in inputs:
    if len(schedule) == 0:
        heapq.heappush(schedule, end)
        continue
    last = heapq.heappop(schedule)
    if last > start:
        heapq.heappush(schedule, last)
    heapq.heappush(schedule, end)
print(len(schedule))

