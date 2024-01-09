# 덱(Deque)

import sys
from collections import deque

commandNum = int(sys.stdin.readline())

result = []
deq = deque()
for i in range(0, commandNum):
    userInput = list(map(str, sys.stdin.readline().split()))
    if userInput[0] == "push_front":
        deq.appendleft(int(userInput[1]))
    elif userInput[0] == "push_back":
        deq.append(int(userInput[1]))
    elif userInput[0] == "pop_front":
        if len(deq)==0:
            result.append(-1)
        else:
            result.append(deq.popleft())
    elif userInput[0] == "pop_back":
        if len(deq)==0:
            result.append(-1)
        else:
            result.append(deq.pop())
    elif userInput[0] == "size":
        result.append(len(deq))
    elif userInput[0] == "empty":
        if len(deq) == 0:
            result.append(1)
        else:
            result.append(0)
    elif userInput[0] == "front":
        if len(deq)==0:
            result.append(-1)
        else:
            result.append(deq[0])
    elif userInput[0] == "back":
        if len(deq)==0:
            result.append(-1)
        else:
            result.append(deq[-1])


for i in result:
    print(i)
