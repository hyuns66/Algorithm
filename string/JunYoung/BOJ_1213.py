# 팰린드롬 만들기

import sys

englishName = sys.stdin.readline().strip()
englishDict = {}

for i in englishName:
    if i in englishDict:
        value = englishDict.get(i)
        englishDict[i] = value + 1
    else:
        englishDict[i] = 1

evenList = []
oddList = []

flag = True
for i in englishDict:
    if (englishDict.get(i)) % 2 == 0:
        for j in range(int(englishDict.get(i)/2)):
            evenList.append(i)
    else:
        if len(oddList) == 0:
            oddList.append(i)
            oddList.append(englishDict.get(i))
        else:
            flag = False
            break

if len(oddList)!=0:
    if oddList[1] != 1:
        for i in range(int(oddList[1] / 2)):
            evenList.append(oddList[0])

answerList = []

if flag:
    if len(oddList) == 0:
        evenList.sort()
        stack = []
        for i in evenList:
            answerList.append(i)
            stack.append(i)
        while len(stack) != 0:
            answerList.append(stack.pop())
    else:
        evenList.sort()
        stack = []
        for i in evenList:
            answerList.append(i)
            stack.append(i)
        answerList.append(oddList[0])
        while len(stack) != 0:
            answerList.append(stack.pop())
    print(''.join(s for s in answerList))

else:
    print("I'm Sorry Hansoo")
