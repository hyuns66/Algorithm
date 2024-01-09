# 나는 친구가 적다 (Small)

import sys

S = sys.stdin.readline()
keyword = sys.stdin.readline()
newS = []

for s in S:
    if s not in ['0','1','2','3','4','5','6','7','8','9']:
        newS.append(s)

S = ''.join(s for s in newS)

if keyword in S:
    print(1)
else:
    print(0)
