# 공약수
import sys

N = int(sys.stdin.readline())
numList = []
commonFactorList = []

userInput = sys.stdin.readline().split()
for i in range(0, N):
    numList.append(int(userInput[i]))

numList.sort()

for i in range(1, numList[0]+1):  # 1~제일작은 숫자 numList[0]
    if N == 2:
        if (numList[0] % i == 0) & (numList[1] % i == 0):
            commonFactorList.append(i)
    else:
        if (numList[0] % i == 0) & (numList[1] % i == 0) & (numList[2] % i == 0):
            commonFactorList.append(i)

for i in range(0, len(commonFactorList)):
    print(commonFactorList[i])
