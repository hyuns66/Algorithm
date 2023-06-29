# 스네이크버드

import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())

fruitHeight = list(map(int, sys.stdin.readline().split()))
fruitHeight.sort()
fd = deque(fruitHeight)

while True:
    if len(fd) == 0:
        break
    if fd[0] <= L:
        fd.popleft()
        L += 1
    else:
        break

print(L)