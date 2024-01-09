# 소수 최소 공배수

import sys
import math


def isPrime(num):
    if num == 2 or num == 3:
        return True

    flag = True
    for j in range(2, int(math.sqrt(num)+1)):
        if num % j == 0:
            flag = False
            break

    if flag:
        return True
    else:
        return False


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
primeList = set()  # A중에서 소수를 담을 리스트

for i in range(0, N):
    if isPrime(A[i]):
        primeList.add(A[i])

if len(primeList) == 0:
    print(-1)
else:
    total = 1
    for prime in primeList:
        total *= prime

    print(total)

"""
반례
5
2 2 2 2 2

5
999983 999997 123 11 97
"""

"""
배운점: 숫자 N의 소수 여부를 판단할 때 숫자 N이 2~루트N까지로 안나눠떨어지면 소수다!
"""