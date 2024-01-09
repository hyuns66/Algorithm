# 복호화

import sys

T = int(sys.stdin.readline())

answerList = []
for i in range(T):
    engDict = {}
    line = sys.stdin.readline().strip().replace(" ", "")

    for i in line:
        if i in engDict:
            value = engDict.get(i)
            engDict[i] = value + 1
        else:
            engDict[i] = 1

    sortedList = sorted(engDict.items(), key=lambda x: x[1], reverse=True)

    max = sortedList[0][1]
    letter = ''
    for i in sortedList:
        if i[1] == max:
            if letter == '':
                letter = i[0]
            else:
                letter='?'
                break

    answerList.append(letter)


for i in answerList:
    print(i)

"""
https://scribblinganything.tistory.com/370 - 문자열 사이에 공백 없애기
"""
