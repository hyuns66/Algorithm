# 큐2

"""import sys

commandNum = int(sys.stdin.readline())

queue = []
result = []
for i in range(0, commandNum):
    userInput = list(map(str, sys.stdin.readline().split()))
    if userInput[0] == "push":
        X = int(userInput[1])
        queue.append(X)
    elif userInput[0] == "pop":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
            del queue[0]
    elif userInput[0] == "size":
        result.append(len(queue))
    elif userInput[0] == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif userInput[0] == "front":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[0])
    elif userInput[0] == "back":
        if len(queue) == 0:
            result.append(-1)
        else:
            result.append(queue[-1])

for i in range(0, len(result)):
    print(result[i])"""

"""
from collections import deque
https://chaewonkong.github.io/posts/python-deque.html

왜 시간초과 떠? 
=> pop을 위해 list의 맨 첫번째 원소를 제거하는 것은 O(N)으로 매우 느립니다.??
=> 젤 앞에껄 빼면, 하나씩 앞으로 땡기느라 느려지는 건가봐..

"""

import sys
from collections import deque

commandNum = int(sys.stdin.readline())

deq = deque()
result = []

for i in range(0, commandNum):
    userInput = list(map(str, sys.stdin.readline().split()))
    if userInput[0] == "push":
        X = int(userInput[1])
        deq.append(X)
    elif userInput[0] == "pop":
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq.popleft())
    elif userInput[0] == "size":
        result.append(len(deq))
    elif userInput[0] == "empty":
        if len(deq) == 0:
            result.append(1)
        else:
            result.append(0)
    elif userInput[0] == "front":
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq[0])
    elif userInput[0] == "back":
        if len(deq) == 0:
            result.append(-1)
        else:
            result.append(deq[-1])

for i in range(0, len(result)):
    print(result[i])
