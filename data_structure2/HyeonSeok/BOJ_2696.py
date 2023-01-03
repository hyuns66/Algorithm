import sys
import heapq

T = int(sys.stdin.readline())
dataset = [list() for i in range(T << 1)]
for t in range(T):
    size = int(sys.stdin.readline())
    dataset[t << 1] = [size]
    for i in range(int(size / 10) + 1):
        dataset[(t << 1) + 1] = dataset[(t << 1) + 1] + (list(map(int, sys.stdin.readline().split())))


for t in range(T):
    answer = list()
    big = list()
    small = list()
    middle, current = 0, 0
    size = dataset[t << 1][0]
    print((size >> 1) + 1)
    for i in range(size):
        current = dataset[(t << 1) + 1][i]
        if i == 0:
            middle = current
            answer.append(middle)
            continue
        if (1 & i) == 0:    # 홀수
            if current <=
        else:    # 짝수
            if current <= middle:
                heapq.heappush(small, current)
            else:
                heapq.heappush(big, current)
    for idx in range(len(answer)):
        if (idx % 10) == 9 or idx == len(answer) - 1:
            print(answer[idx], end = "\n")
        else:
            print(answer[idx], end = " ")
