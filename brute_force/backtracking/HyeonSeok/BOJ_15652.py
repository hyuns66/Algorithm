import sys

def backTracking(startNode):
    global N, M, stack
    if len(stack)==M:
        print(*stack)
        return
    for j in range(startNode, N):
        stack.append(j+1)
        backTracking(j)
        stack.pop()

N, M = map(int, sys.stdin.readline().split())
stack = list()
for i in range(N):
    stack.append(i+1)
    backTracking(i)
    stack.pop()