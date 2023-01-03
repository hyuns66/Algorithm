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
