# 세로읽기

import sys

board = []
m = 0
for i in range(0, 5):
    line = sys.stdin.readline().strip()
    if len(line) > m:
        m = len(line)
    board.append(line)

answer = []

count = 0
while count < m:
    for j in range(0, 5):
        if count < len(board[j]):
            answer.append(board[j][count])
    count += 1

result = ''.join(answer) # 이렇게 하면 리스트를 이어서 하나의 문자열로 만들어 줄 수 있다.
print(result)

