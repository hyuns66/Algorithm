# 스택 수열

import sys

N = int(sys.stdin.readline())
sequence = []
stack = []
answer = []

for i in range(N):
    sequence.append(int(sys.stdin.readline()))

index = 0
num = 0
while True:

    if len(stack) == 0:
        if num + 1 <= N:
            num += 1
            stack.append(num)
            answer.append("+")
        else:
            answer.clear()
            answer.append("NO")
            break
    elif stack[-1] != sequence[index]:
        if num + 1 <= N:
            num += 1
            stack.append(num)
            answer.append("+")
        else:
            answer.clear()
            answer.append("NO")
            break
    else:
        stack.pop()
        answer.append("-")
        index += 1

    if index == len(sequence):
        break

for i in answer:
    print(i)
