# 스택

import sys

commandNum = int(sys.stdin.readline())

stack = []
result = []
for i in range(0, commandNum):
    userInput = list(map(str, sys.stdin.readline().split()))
    if userInput[0] == "push":
        X = int(userInput[1])
        stack.append(X)
    elif userInput[0] == "pop":
        if len(stack) - 1 < 0:
            result.append(-1)
        else:
            #stack.remove(len(stack) - 1)  # 가장 위에 있는 정수 빼기
            result.append(stack[-1])
            del stack[len(stack) - 1]
    elif userInput[0] == "size":
        result.append(len(stack))
    elif userInput[0] == "empty":
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif userInput[0] == "top":
        if len(stack) - 1 < 0:
            result.append(-1)
        else:
            result.append(stack[-1])

for i in range(0, len(result)):
    print(result[i])
    