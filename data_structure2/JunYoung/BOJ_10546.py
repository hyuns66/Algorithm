# 배부른 마라토너

import sys

N = int(sys.stdin.readline())
participants = {}
for _ in range(N):
    name = sys.stdin.readline().strip()
    if name in participants:
        participants[name] += 1
    else:
        participants[name] = 1

for _ in range(N-1):
    name = sys.stdin.readline().strip()
    if name in participants:
        if participants[name] == 1:
            del participants[name]
        else:
            participants[name] -= 1

for i in participants.keys():
    print(i)

