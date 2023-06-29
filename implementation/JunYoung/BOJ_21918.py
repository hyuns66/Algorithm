# 전구

import sys

N, M = map(int, sys.stdin.readline().split())
state = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        state[b - 1] = c
    elif a == 2:
        for j in range(b - 1, c):
            if state[j] == 0:
                state[j] = 1
            else:
                state[j] = 0
    elif a == 3:
        for j in range(b - 1, c):
            state[j] = 0
    elif a == 4:
        for j in range(b - 1, c):
            state[j] = 1

for i in state:
    print(i, end=" ")
