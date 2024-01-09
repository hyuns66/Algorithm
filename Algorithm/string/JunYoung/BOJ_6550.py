# 부분 문자열 (실버5)

import sys
from collections import deque

result = []
f = open("BOJ_6550_input.txt", 'r')
lines = f.readlines()
for line in lines:
    s, t = map(str, line.strip().split())
    s = deque(s)

    for i in range(0, len(t)):
        if len(s) == 0:
            break

        if t[i] == s[0]:
            s.popleft()

    if len(s) == 0:
        result.append("Yes")
    else:
        result.append("No")

for i in result:
    print(i)
f.close()

"""
# 부분 문자열 (실버5) - 제출용

import sys
from collections import deque

result = []
lines = sys.stdin.readlines()
for line in lines:
    s, t = map(str, line.strip().split())
    s = deque(s)

    for i in range(0, len(t)):
        if len(s) == 0:
            break
            
        if t[i] == s[0]:
            s.popleft()
     
    if len(s) == 0:
        result.append("Yes")
    else:
        result.append("No")

for i in result:
    print(i)
"""