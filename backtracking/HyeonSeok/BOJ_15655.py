import sys

def backTracking(idx):
    global N, M, num_list, stack
    if len(stack)==M:
        print(*stack)
        return
    for i in range(idx+1, N):
        stack.append(num_list[i])
        backTracking(i)
        stack.pop()

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
stack = list()

for idx, num in enumerate(num_list):
    stack.append(num)
    backTracking(idx)
    stack.pop()