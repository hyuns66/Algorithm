# A->B

import sys
import math

A, B = map(int, sys.stdin.readline().split())
count = 0
flag = True

while B > A:
    if B % 10 == 1:
        B = int(math.trunc(B / 10)) #1의 자리 버리기
        count += 1
    elif (B % 2) == 0:
        B = int(B / 2)
        count += 1
    else:
        flag = False
        break
    #print(B)

if not flag:
    print(-1)
else:
    if B == A:
        print(count+1)
    else:
        print(-1)
