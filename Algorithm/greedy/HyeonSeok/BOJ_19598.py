import sys
import heapq

N = int(sys.stdin.readline())
heap = list()
for _ in range(N):
    start, end = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (start, "start"))
    heapq.heappush(heap, (end, "end"))

answer = 0
height = 0
while heap:
    position, point = heapq.heappop(heap)
    if point == "start":
        height += 1
        answer = max(height, answer)
    else:
        height -= 1
print(answer)
