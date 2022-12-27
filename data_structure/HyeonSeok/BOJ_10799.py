import sys
from collections import deque

laser = deque(list(sys.stdin.readline()))
laser.pop()

temp = 0
answer = 0
stack = list()

for i in range(len(laser)):
    if laser[i] == '(':
        temp += 1
        stack.append(laser[i])
    else:
        if laser[i-1] == '(':
            temp -= 1
            answer += temp
            stack.pop()
        elif laser[i-1] == ')':
            temp -= 1
            answer += 1
            stack.pop()

print(answer)