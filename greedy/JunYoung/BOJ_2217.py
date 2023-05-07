# 로프

import sys

N = int(sys.stdin.readline())
roap = []
for i in range(N):
    r = int(sys.stdin.readline())
    roap.append(r)

roap.sort(reverse=True)
for i in range(N):
    roap[i] = (i+1) * roap[i]

roap.sort(reverse=True)
print(roap[0])
