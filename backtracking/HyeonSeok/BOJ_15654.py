import sys

def backTracking():
    global N, M, stack, num_list
    if len(stack)==M:
        print(*stack)
        return
    for idx, j in enumerate(num_list):
        if not visited[idx]:
            stack.append(j)
            visited[idx] = True
            backTracking()
            visited[idx] = False
            stack.pop()
        
        
N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
visited = [False for _ in range(N)]
stack = list()
for idx, num in enumerate(num_list):
    stack.append(num)
    visited[idx] = True
    backTracking()
    stack.pop()
    visited[idx] = False