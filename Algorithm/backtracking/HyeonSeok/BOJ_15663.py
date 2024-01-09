import sys

def backTracking():
    global N, M, num_list, stack, stack_cache
    if len(stack)==M and tuple(stack) not in stack_cache:
        print(*stack)
        stack_cache.add(tuple(stack))
        return
    for i, n in enumerate(num_list):
        if not visited[i]:
            stack.append(n)
            visited[i] = True
            backTracking()
            stack.pop()
            visited[i] = False

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
visited = [False for _ in range(N)]
stack_cache = set()
stack = list()
num_list.sort()

for i, num in enumerate(num_list):
    stack.append(num)
    visited[i] = True
    backTracking()
    stack.pop()
    visited[i] = False