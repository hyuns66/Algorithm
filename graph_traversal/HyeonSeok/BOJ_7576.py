import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatos = list()
start_node = list()

for y in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for x, value in enumerate(temp):
        if value == 1:
            start_node.append((y, x, value))
    tomatos.append(temp)
    
queue = deque()
for s in start_node:
    queue.append(s)

while queue:
    y, x, value = queue.popleft()
    for dir in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        dir_y = y + dir[0]
        dir_x = x + dir[1]
        if dir_y < 0 or dir_y >= N or dir_x < 0 or dir_x >= M:
            continue
        if tomatos[dir_y][dir_x] == 0:
            tomatos[dir_y][dir_x] = value + 1
            queue.append((dir_y, dir_x, value+1))

answer = 0
for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 0:
            print(-1)
            exit(0)
        answer = max(answer, tomatos[y][x])
print(answer-1)