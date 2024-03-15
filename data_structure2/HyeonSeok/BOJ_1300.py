import sys
import heapq

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())
h = list()
for y in range(1, N+1):
    for x in range(1, N+1):
        heapq.heappush(h, y*x)
        
answer = 0
for _ in range(k):
    answer = heapq.heappop(h)
print(answer)