import sys
import heapq

maxHeap = []
minHeap = []
T = int(sys.stdin.readline())

for i in range(T):
    Q = int(sys.stdin.readline())
    for i in range(Q):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(maxHeap, -num)
            heapq.heappush(minHeap, num)
        else:
            if not maxHeap:
                continue
            elif num == -1:
                heapq.heappop(minHeap)
                heapq.