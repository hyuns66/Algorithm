# 절댓값 힙

import sys
import heapq

N = int(sys.stdin.readline())

negativeHeap = []
positiveHeap = []
answer = []

for i in range(N):
    calculation = int(sys.stdin.readline())
    if calculation != 0:
        if calculation < 0:
            heapq.heappush(negativeHeap, -calculation)  # 최대 힙
        else:
            heapq.heappush(positiveHeap, calculation)  # 최소 힙
    else:
        #print(negativeHeap)
        #print(positiveHeap)
        if len(negativeHeap) != 0 and len(positiveHeap) != 0:
            if negativeHeap[0]<=positiveHeap[0]:
                answer.append(-(heapq.heappop(negativeHeap)))
            else:
                answer.append((heapq.heappop(positiveHeap)))
        elif len(negativeHeap) != 0:
            answer.append(-(heapq.heappop(negativeHeap)))
        elif len(positiveHeap) != 0:
            answer.append((heapq.heappop(positiveHeap)))
        else:
            answer.append(0)

for i in answer:
    print(i)
