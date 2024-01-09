# 홀수 홀릭 호석이

import sys
from itertools import combinations

N = int(sys.stdin.readline())

gminOdd = 0
gmaxOdd = 0


def operation(N, flag): # flag가 1이면 min/ 2면 max
    global gminOdd, gmaxOdd
    strN = str(N)

    # 홀수 수 계산
    if flag == 1:
        for i in strN:
            if int(i) % 2 != 0:
                gminOdd += 1
        print(gminOdd)
    else:
        for i in strN:
            if int(i) % 2 != 0:
                gmaxOdd += 1

    if len(strN) == 1:
        return
    elif len(strN) == 2:
        newNum = int(strN[0]) + int(strN[1])
        operation(newNum, flag)
    else:

        # 자를 수 있는 부분 계산
        cutPoint = []
        for i in range(1, len(strN)):
            cutPoint.append(i)
        combs = list(combinations(cutPoint, 2))
        #print(combs)

        # 가능한 홀수 수의 최소 최댓값 계산
        minOdd = sys.maxsize
        mincomb = []
        maxOdd = 0
        maxcomb = []
        for c in combs:
            temp = []
            temp.append(int(strN[0:c[0]]))
            temp.append(int(strN[c[0]:c[1]]))
            temp.append(int(strN[c[1]:]))

            oddsNum = 0
            sum = 0
            for i in temp:
                sum += i
            for i in (str(sum)):
                if int(i) % 2 !=0:
                    oddsNum += 1

            # 최솟값, 최댓값 갱신
            if oddsNum < minOdd:
                minOdd = oddsNum
                mincomb = sum
            if oddsNum > maxOdd:
                maxOdd = oddsNum
                maxcomb = sum

        if flag == 1:
            print(mincomb)
            operation(sum, 1)
        else:
            operation(sum, 2)


operation(N, 1)
operation(N, 2)
print(gmaxOdd, gminOdd)
