import sys

def backTracking():
    global N, M, visited, stack
    if len(stack)==M:
        print(*stack)
        return
    for i in range(1, N+1):
        if not visited[i-1]:
            visited[i-1] = True
            stack.append(i)
            backTracking()
            visited[i-1] = False
            stack.pop()

N, M = map(int, sys.stdin.readline().split())
stack = list()
visited = [False for n in range(N)]
for i in range(1, N+1):
    stack = [i]
    visited[i-1] = True
    backTracking()
    visited[i-1] = False