# 제로

import sys

K = int(sys.stdin.readline())

stack = []
for i in range(K):
    val = int(sys.stdin.readline())
    if val == 0:
        stack.pop()
    else:
        stack.append(val)

print(sum(stack))