import sys

stack = []
top = -1
result = []


def push(i):
    global top
    top += 1
    stack.append(i)


def pop():
    global top
    if(top>=0):
        top -= 1
        return stack.pop()
    else:
        return -1


def whatistop():
    global top
    if(top >= 0):
        return stack[top]
    else:
        return -1

def empty():
    global top
    return 0 if top >= 0 else 1

N = int(input())
for i in range(N):
    command = sys.stdin.readline()
    rCommand = command.split()
    if rCommand[0] == "push":
        push(rCommand[1])
    elif rCommand[0] == "pop":
        result.append(pop())
    elif rCommand[0] == "size":
        result.append(len(stack))
    elif rCommand[0] == "empty":
        result.append(empty())
    elif rCommand[0] == "top":
        result.append(whatistop())

for i in range(len(result)):
    print(result[i])