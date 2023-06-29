# 0의 개수

import sys

T = int(sys.stdin.readline())

answer = []
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    count = 0
    while True:
        if N > M:
            break
        for j in str(N):
            if j == '0':
                count += 1
        N += 1
    answer.append(count)

for i in answer:
    print(i)
