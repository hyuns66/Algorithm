import sys
from collections import deque

N = int(sys.stdin.readline())
testcase = [list() for i in range(N)]
data = [deque() for j in range(N)]
mask = [deque() for k in range(N)]

for i in range(N):
    testcase[i] = list(map(int, sys.stdin.readline().split()))
    data[i] = deque(list(map(int, sys.stdin.readline().split())))
    mask[i] = deque([m for m in range(testcase[i][0])])

for i in range(N):  # testcase 반복
    while True:
        cnt = 0
        for j in range(testcase[i][0]-1, -1, -1):   # 큐 뒤쪽 부터 탐색 (출력되는 부분부터 탐색)
            maxIdx = data[i].index(max(data[i]))
            data[i].rotate(j - maxIdx)
            mask[i].rotate(j - maxIdx)
            data[i].pop()
            cnt += 1
            if mask[i].pop() == testcase[i][1]:
                print(cnt)
                break
        break
