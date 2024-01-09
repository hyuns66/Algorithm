import sys

def backTracking(startNode):
    global N, M, stack, i
    if len(stack) >= M:
        print(*stack)
        return
    for j in range(startNode+1, N):
        stack.append(j+1)
        backTracking(j)
        stack.pop()

N, M = map(int, sys.stdin.readline().split())
stack = list()
for i in range(N-M+1):
    stack = [i+1]
    backTracking(i)