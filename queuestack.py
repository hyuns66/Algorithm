from collections import deque

N = int(input())
qstack = list(map(int, input().split()))
q = deque()
nums = list(map(int, input().split()))
for idx, n in enumerate(nums):
    if qstack[idx] == 0:
        q.append(n)

M = int(input())
answer = list()
order = list(map(int, input().split()))
for o in order:
    q.appendleft(o)
    answer.append(q.pop())

print(*answer)