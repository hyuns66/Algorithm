# 숫자의 합

import sys

N = int(sys.stdin.readline())
numberString = sys.stdin.readline()

totalSum = 0
for i in range(0, N):
    totalSum += int(numberString[i])

print(totalSum)