import heapq
import sys

N = int(sys.stdin.readline())
heap = list()
answer = list()


def pop():
    if len(heap) == 0:
        answer.append(0)
    else:
        answer.append(heapq.heappop(heap)[1])


for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        pop()
    else:
        heapq.heappush(heap, (abs(num), num))

for i in range(len(answer)):
    print(answer[i])