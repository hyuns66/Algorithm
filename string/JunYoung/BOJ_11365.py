# !밀비 급일

import sys

stack = []
answer = []
while True:
    line = sys.stdin.readline().strip()
    if line == "END":
        break
    else:
        for i in line:
            stack.append(i)
        for i in range(len(line)):
            answer.append(stack.pop())
        answer.append('\n')

for i in range(len(answer)):
    print(answer[i], end='')
