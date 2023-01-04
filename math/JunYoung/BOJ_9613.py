# GCD 합

import sys
from math import gcd

t = int(sys.stdin.readline())
result = []
for i in range(0, t):
    testcase = list(map(int, sys.stdin.readline().split()))
    n = testcase[0]
    totalGCD = 0
    for j in range(0, n - 1):
        for k in range(j + 1, n):
            totalGCD += gcd(testcase[j + 1], testcase[k + 1])
    result.append(totalGCD)

for i in range(0, t):
    print(result[i])

# math 함수 이용해봤다!
