import sys
import heapq

answer = list()
T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    heapSize = 0
    maxHeap = []
    minHeap = []
    cnt = 0
    mask = list()
    for j in range(k):
        op, num = sys.stdin.readline().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(maxHeap, (-num, cnt))
            heapq.heappush(minHeap, (num, cnt))
            mask.append(True)
            heapSize += 1
            cnt += 1
        elif op == 'D':
            if heapSize <= 0:
                continue
            if num == 1:
                while maxHeap and not mask[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    q = heapq.heappop(maxHeap)
                    mask[q[1]] = False
                    heapSize -= 1
            else:
                while minHeap and not mask[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    q = heapq.heappop(minHeap)
                    mask[q[1]] = False
                    heapSize -= 1
    while minHeap and not mask[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and not mask[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    if heapSize == 0:
        answer.append("EMPTY")
    else:
        answer.append((minHeap[0][0], -(maxHeap[0][0])))

for i in range(len(answer)):
    if type(answer[i]) is str:
        print(answer[i])
    else:
        print(answer[i][1], answer[i][0])