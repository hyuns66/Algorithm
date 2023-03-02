# 최대 힙

import sys
import heapq

N = int(sys.stdin.readline())
heap = []
answer = []

for i in range(N):
    calculation = int(sys.stdin.readline())
    if calculation != 0:
        heapq.heappush(heap, -calculation)
    else:
        if len(heap) != 0:
            answer.append(-heapq.heappop(heap))
        else:
            answer.append(0)

for i in answer:
    print(i)


#힙의 개념
#https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html
#
