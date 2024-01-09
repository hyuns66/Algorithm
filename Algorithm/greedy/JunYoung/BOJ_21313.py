# 문어

import sys

N = int(sys.stdin.readline())

answer = []
if N % 2 == 0:
    num = 1
    for i in range(N):
        if num == 3:
            num = 1
        answer.append(num)
        num += 1
else:
    num = 1
    for i in range(N - 1):
        if num == 3:
            num = 1
        answer.append(num)
        num += 1
    answer.append(3)

for i in answer:
    print(i, end=' ')
