import sys
import heapq

T = int(sys.stdin.readline())
heap = list()

for t in range(T):
    size = int(sys.stdin.readline())
    dataset = list(map(int, sys.stdin.readline().split()))
    answer = list()
    temp = list()
    for i in range(size):
        while temp:
            heapq.heappush(heap, temp.pop())
        heapq.heappush(heap, dataset[i])
        heapq.heapify(heap)
        if (1 & i) == 0:    # 홀수
            for j in range(i >> 1):
                temp.append(heapq.heappop(heap))
            answer.append(heap[0])
    print(*answer)

