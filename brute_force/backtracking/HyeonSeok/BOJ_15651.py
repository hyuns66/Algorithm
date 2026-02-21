import sys

def backTracking():
    global N, M, stack
    if len(stack)==M:
        print(*stack)
        return
    for j in range(N):
        stack.append(j+1)
        backTracking()
        stack.pop()

N, M = map(int, sys.stdin.readline().split())
stack = list()
for i in range(N):
    stack.append(i+1)
    backTracking()
    stack.pop()