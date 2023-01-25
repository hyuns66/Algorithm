# 다음 소수
import math
import sys

N = int(sys.stdin.readline())
testNum = []
ans = []


def isPrime(x):
    if x == 0 or x == 1:
        return False

    for i in range(2, int(math.sqrt(x)) + 1):  # 루트2는 1.414이다.
        if x % i == 0:
            return False

    return True


for i in range(N):
    testNum.append(int(sys.stdin.readline()))

for i in range(N):
    z = testNum[i]
    while True:
        if isPrime(z):
            ans.append(z)
            break
        else:
            z += 1

for i in ans:
    print(i)

"""
참고:
https://steadily-worked.tistory.com/705
"""
