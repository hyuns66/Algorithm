# 패션왕 신해빈

import sys
from itertools import product

T = int(sys.stdin.readline())

answer = []
for _ in range(T):
    N = int(sys.stdin.readline())
    closet = {}
    for _ in range(N):
        cloth, category = map(str, sys.stdin.readline().split())
        if category in closet:
            closet[category] = closet[category] + [cloth]
        else:
            closet[category] = [cloth]

    #print(closet)
    numberList = []
    for i in closet.keys():
        numberList.append(len(closet[i])+1)

    total = 1
    for i in numberList:
        total *= i
    answer.append(total-1)

    """categoryNum = len(numberList)
    masking = []
    #print(numberList)
    for i in range(2 ** categoryNum):
        # masking.append(bin(i))
        masking.append(format(i, 'b').zfill(categoryNum))
    #print(masking)

    total = 0
    for combination in product([0, 1], repeat=len(numberList)):
        add = 0
        for i, c in enumerate(combination): #enumerate 함수는 (인덱스, 원소)의 형태의 튜플을 반환합니다.
            if c == 1:
                if add == 0:
                    add = numberList[i]
                else:
                    add = add * numberList[i]
        total += add
    answer.append(total)"""

for i in answer:
    print(i)


