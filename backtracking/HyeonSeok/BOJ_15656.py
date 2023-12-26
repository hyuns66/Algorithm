import sys

def backTracking():
    global N, M, stack, num_list
    if len(stack)==M:
        print(*stack)
        return
    for n in num_list:
        stack.append(n)
        backTracking()
        stack.pop()

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
stack = list()
num_list.sort()

for num in num_list:
    stack.append(num)
    backTracking()
    stack.pop()