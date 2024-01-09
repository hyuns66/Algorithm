import sys
from collections import deque

N = int(sys.stdin.readline())
answer = list()
q = deque()

for _ in range(N):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        temp = -1 if (len(q) == 0) else q.popleft()
        answer.append(temp)
    elif cmd[0] == "size":
        answer.append(len(q))
    elif cmd[0] == "empty":
        answer.append(1 if len(q)==0 else 0)
    elif cmd[0] == "front":
        answer.append(-1 if len(q)==0 else q[0])
    elif cmd[0] == "back":
        answer.append(-1 if len(q)==0 else q[-1])

for a in answer:
    print(a)