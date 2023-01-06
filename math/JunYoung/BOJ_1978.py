# 소수 찾기

import sys

primeCount = 0

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

for i in range(0, N):
    flag = False

    if numList[i] == 2:  # 숫자 2 예외처리 해 줌
        primeCount += 1

    for j in range(2, numList[i]):  # 나누는 숫자가 2부터 시작하니까 숫자 2는 예외처리 필요
        flag = True
        if numList[i] % j == 0:
            flag = False
            break  # 소수가 아니다

    if flag:
        primeCount += 1

print(primeCount)
