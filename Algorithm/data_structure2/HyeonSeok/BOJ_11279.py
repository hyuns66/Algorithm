import sys
import heapq
from collections import deque

N = sys.stdin.readline()
N = int(N)
heap = []
result = deque()

for i in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        if heap:
            result.append(-(heapq.heappop(heap)))
        else:
            result.append(0)

while result:
    print(result.popleft())