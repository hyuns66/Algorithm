from collections import deque
import sys

N = int(input())
numList = list()
stack = list()
stackCnt = 1
result = deque()

def error():
    print("NO")
    sys.exit(0)

def push():
    global stackCnt
    result.appendleft('+')
    stack.append(stackCnt)
    if stackCnt > N:
        error()
    else:
        stackCnt += 1

def pop():
    result.appendleft('-')
    stack.pop()

for i in range(N):
    num = int(sys.stdin.readline())
    numList.append(num)

for i in numList:
    while True:
        if not stack:
            push()
        elif stack[-1] != i:
            if stackCnt > i:
                error()
            push()
        else:
            pop()
            break

while result:
    print(result.pop())