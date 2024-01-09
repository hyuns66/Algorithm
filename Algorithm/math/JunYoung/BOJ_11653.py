# 소인수 분해 Factorization

import sys

N = int(sys.stdin.readline())

factor = []
left = N

while left != 1:
    for i in range(2, left+1):
        if left % i == 0:
            factor.append(i)
            left = int(left / i)
            break

for i in range(0, len(factor)):
    print(factor[i])
