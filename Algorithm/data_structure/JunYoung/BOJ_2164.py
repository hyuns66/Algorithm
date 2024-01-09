# 카드2

import sys
from collections import deque

N = int(sys.stdin.readline())

deq = deque()
for i in range(0, N):
    deq.append(i+1)

while len(deq)!=1:
    deq.popleft()
    deq.rotate(-1)

print(deq.pop())