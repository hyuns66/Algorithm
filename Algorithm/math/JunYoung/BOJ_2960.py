# 에라토스테네스의 체

import sys

N, K = map(int, sys.stdin.readline().split())

numList = []
eraseList = []
for i in range(2, N+1):
    numList.append(i)

while True:
    P = numList[0]
    for i in numList:
        if i % P == 0:  # P와 P의 배수 지우기
            numList.remove(i)
            eraseList.append(i)
    if len(numList) == 0:
        break

print(eraseList[K-1])

"""
이 알고리즘은 다음과 같다.

1) 2부터 N까지 모든 정수를 적는다.
2) 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
3) P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
4) 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

"""
