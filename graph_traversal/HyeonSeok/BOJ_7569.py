import copy
import sys

M, N, H = map(int, sys.stdin.readline().split())
box = [[list() for j in range(N)]for k in range(H)]
visited = [[[False for c in range(M)] for a in range(N)]for b in range(H)]
day = -1


def DFS(stack):
    global day, visited, box
    day += 1
    new_stack = list()
    while stack:
        _z, _y, _x = stack.pop()
        if not visited[_z][_y][_x]:
            visited[_z][_y][_x] = True
            for dz in range(-1, 2):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if not (dz * dx == 0 and dy * dx == 0 and dz * dy == 0):
                            continue
                        if 0 <= _z + dz < H and 0 <= _y + dy < N and 0 <= _x + dx < M:
                            if box[_z + dz][_y + dy][_x + dx] == 0:
                                new_stack.append((_z + dz, _y + dy, _x + dx))
                                box[_z + dz][_y + dy][_x + dx] = 1
    return new_stack


# 1 : 익토, 0 : 안익토, -1 : 없토
for z in range(H):
    for y in range(N):
        box[z][y] = list(map(int, sys.stdin.readline().split()))

tomato = list()
flag = True
for z in range(H):
    for y in range(N):
        for x in range(M):
            if box[z][y][x] == 1:
                tomato.append((z, y, x))
            elif box[z][y][x] == 0:
                flag = False
            else:
                visited[z][y][x] = True

if flag:
    print(0)
    exit(0)

while tomato:
    temp = DFS(tomato)
    tomato = copy.deepcopy(temp)

for v in visited:
    for b in v:
        if False in b:
            print(-1)
            exit(0)

print(day)