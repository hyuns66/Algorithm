from collections import deque

def dice_rol(dice_row, dice_col, direction, position):
    dir_col = direction[0]
    dir_row = direction[1]
    if dir_row == 1:    # 우
        temp = dice_row[-1]
        dice_row[-1] = dice_col[-1]
        dice_col[-1] = temp
        dice_row.rotate(dir_row)
        dice_col[1] = dice_row[1]
    elif dir_row == -1: # 좌
       temp = dice_row[0]
       dice_row[0] = dice_col[-1]
       dice_col[-1] = temp
       dice_row.rotate(dir_row)
       dice_col[1] = dice_row[1]
    else:  # 상, 하
       dice_col.rotate(dir_col)
       dice_row[1] = dice_col[1]
    position[0] += dir_col
    position[1] += dir_row
       
def rotate(A, B, direction):
    if A > B:   # 시계방향
        temp = direction[0]
        direction[0] = direction[1]
        direction[1] = -temp
    elif A < B: # 반시계 방향
        temp = direction[1]
        direction[1] = direction[0]
        direction[0] = -temp

def get_point(graph, position):
    num = graph[position[0]][position[1]]
    stack = list()
    count = 1
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    stack.append(position)
    visited[position[0]][position[1]] = True
    while stack:
        y, x = stack.pop()
        for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            py = y+dy
            px = x+dx
            if py < 0 or py >= len(graph) or px < 0 or px >= len(graph[0]):
                continue
            if graph[py][px] == num and not visited[py][px]:
                stack.append((py, px))
                count += 1
                visited[py][px] = True
    return num * count

N, M, K = map(int, input().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))
position = [0, 0]
direction = [0, 1]
dice_row = deque([4, 1, 3])
dice_col = deque([2, 1, 5, 6])
answer = 0

for _ in range(K):
    py = position[0] + direction[0]
    px = position[1] + direction[1]
    if py < 0 or py >= N or px < 0 or px >= M:
        direction[0] = -direction[0]
        direction[1] = -direction[1]
    dice_rol(dice_row, dice_col, direction, position)
    answer += get_point(graph, position)
    rotate(dice_col[-1], graph[position[0]][position[1]], direction)

print(answer)