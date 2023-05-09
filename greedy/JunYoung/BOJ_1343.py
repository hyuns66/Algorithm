# 폴리오미노

import sys

board = sys.stdin.readline().strip()

polyLen = []
start = 0
#print(len(board))
for i in range(len(board)):
    if board[i] == ".":
        if start != i:
            #print(i)
            polyLen.append(i - start)
        start = i + 1
    elif i == len(board) - 1:
        polyLen.append(i - start + 1)

#print(polyLen)

answer = []
for i in polyLen:
    num = i
    while num > 0:
        if num - 4 >= 0:
            answer.append('A')
            answer.append('A')
            answer.append('A')
            answer.append('A')
            num -= 4
        elif num - 2 >= 0:
            answer.append('B')
            answer.append('B')
            num -= 2
        else:
            num = -1

    if num == -1:
        answer.clear()
        answer.append(-1)
        break

c = 0
if len(answer) == 1:
    print(answer[0])
else:
    for i in board:
        if i == "X":
            print(answer[c], end='')
            c += 1
        else:
            print(".",end='')
