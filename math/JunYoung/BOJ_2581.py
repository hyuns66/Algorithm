# 소수

import sys

primeList = []
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

for num in range(M, N + 1):
    flag = True
    if num == 1:
        flag = False
    else:
        for i in range(2, num):
            if num == 2:
                flag = True
                break
            if num % i == 0:
                flag = False
                break

    if flag:
        primeList.append(num)

if len(primeList) == 0:
    print(-1)
else:
    print(sum(primeList))
    print(primeList[0])


"""
 소수 1에 대한 처리로 인한 오답
"""