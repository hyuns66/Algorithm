# 괄호

import sys

N = int(sys.stdin.readline())

result = []
for i in range(0, N):
    testString = sys.stdin.readline()
    stack = []
    flag = True
    for i in range(0, len(testString)):
        if testString[i] == "(":
            stack.append("(")
        elif testString[i] == ")":
            if len(stack) == 0:
                flag = False
                break
            else:
                stack.pop()

    if len(stack) != 0:
        flag = False

    if flag:
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)
