# LCM
# Least Common Multiple

import sys

N = int(sys.stdin.readline())  # 테스트 횟수
result = []

for i in range(0, N):
    numList = []
    userInput = sys.stdin.readline().split()
    numList.append(int(userInput[0]))
    numList.append(int(userInput[1]))
    numList.sort()
    for j in range(1, numList[1] + 1):
        if ((numList[0] * j) >= numList[1]) & (((numList[0] * j) % numList[1]) == 0):
            result.append(numList[0] * j)  # 최소 공배수
            break  # 찾으면 for 루프 탈출

for i in range(0, N):
    print(result[i])

#다른 사람 코드 오... lcm이라는 함수가 있어.
#from math import lcm
#t = int(input())
#for _ in range(t):
#    a, b = map(int, input().split())
#    print(lcm(a, b))