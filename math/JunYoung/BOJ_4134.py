# 다음 소수 - 원래 코드 왜 안 됐는지 생각 해보기
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
<원래 코드>
while True:
    for j in range(N):
        if (num >= testNum[j]) and isPrime(num):
            if ans[j] == 0:
                ans[j] = num

    num += 1
    flag = True
    for s in range(N):
        if ans[s] == 0:
            flag = False

    if flag:
        break
"""

"""
참고:
https://steadily-worked.tistory.com/705
"""
