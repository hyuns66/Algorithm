# 서강근육맨

import sys

N = int(sys.stdin.readline())
muscleLoss = list(map(int, sys.stdin.readline().split()))

muscleLoss.sort()

muscleLossMax = 0
if N % 2 == 0:
    for i in range(int(N / 2)):
        sum = muscleLoss[i] + muscleLoss[-(i+1)]
        if sum > muscleLossMax:
            muscleLossMax = sum
else:
    if N == 1:
        if muscleLoss[0] > muscleLossMax:
            muscleLossMax = muscleLoss[0]
    else:
        #print(int((N - 1) / 2))
        for i in range(int((N - 1) / 2)):  # 마지막 이전꺼 비교
            sum = muscleLoss[i] + muscleLoss[-(i+1) - 1]
            #print(str(i)+":")
            #print(muscleLoss[-i - 1])
            if sum > muscleLossMax:
                muscleLossMax = sum
        if muscleLoss[-1] > muscleLossMax:  # 마지막꺼 비교
            muscleLossMax = muscleLoss[-1]

print(muscleLossMax)
