# 귀찮음

cost = 0


def cutStick(inputList):
    global cost
    if len(inputList) == 1:
        return 
    Anum = len(inputList) // 2
    Bnum = len(inputList) - Anum
    Asize = 0
    Bsize = 0
    for i in range(Anum):
        Asize += inputList[i]
    for i in range(Bnum):
        Bsize += inputList[Anum + i]
    cost += Asize * Bsize
    #print(str(Asize * Bsize) + "더해짐")
    cutStick(inputList[:Anum])
    cutStick(inputList[Anum:])


import sys

n = map(int, sys.stdin.readline())
stickSize = list(map(int, sys.stdin.readline().split()))

stickSize.sort()
#print(stickSize)

cutStick(stickSize)
print(cost)

# a+b의 막대를 a/b로 자를 때 최소비용으로 되려면 a가 가능한 젤 작은 숫자여야하는 것 같다!
# 그래서 자르고 싶은 막대 중 두동강 낼때 절반 또는 홀수의 경우 num//2의 수로 젤 작게 만들 수 있는 한 파트, 남은걸로 다른 한 파트를 만들어서 잘랐다.
