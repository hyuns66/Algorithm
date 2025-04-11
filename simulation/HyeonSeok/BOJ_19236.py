import copy

def move(graph, pos):
    dirs = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    for i in range(1, len(pos)):
        y, x = pos[i]
        # 물고기 없는 위치면 패스
        if y == -1 or x == -1 or graph[y][x][0] <= 0:
            continue
        ai, bi = graph[y][x]
        dy, dx = dirs[bi]
        # 방향 업데이트
        while y+dy < 0 or y+dy >= 4 or x+dx < 0 or x+dx >= 4 or graph[y+dy][x+dx][0] == -1:
            bi = (bi+1)%8
            dy, dx = dirs[bi]
        # 이동 (위치 바꾸기)
        if graph[y+dy][x+dx][0] > 0:
            temp = copy.deepcopy(pos[i])
            pos[i] = copy.deepcopy(pos[graph[y+dy][x+dx][0]])
            pos[graph[y+dy][x+dx][0]] = copy.deepcopy(temp)
        else:
            pos[i] = [y+dy, x+dx]
        temp = copy.deepcopy(graph[y+dy][x+dx])
        graph[y+dy][x+dx] = [graph[y][x][0], bi]
        graph[y][x] = copy.deepcopy(temp)

def eat_fish(graph, pos, sy, sx, ty, tx):
    fish_num = graph[ty][tx][0]
    pos[fish_num] = [-1, -1]
    pos[0] = [ty, tx]
    graph[sy][sx][0] = 0
    graph[ty][tx][0] = -1
    return fish_num
        
def back_tracking(graph, pos, eat_sum):
    global answer
    new_graph = copy.deepcopy(graph)
    new_pos = copy.deepcopy(pos)
    move(new_graph, new_pos)

    # 상어위치
    sy, sx = new_pos[0]
    dirs = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    ts_dy, ts_dx = dirs[new_graph[sy][sx][1]]
    s_dy, s_dx = (ts_dy, ts_dx)
    count = 1
    flag = True
    while sy+s_dy >= 0 and sy+s_dy < 4 and sx+s_dx >= 0 and sx+s_dx < 4:
        if new_pos[new_graph[sy+s_dy][sx+s_dx][0]][0] == -1 or new_graph[sy+s_dy][sx+s_dx][0] <= 0:
            count += 1
            s_dy = ts_dy * count
            s_dx = ts_dx * count
            continue
        eat_graph = copy.deepcopy(new_graph)
        eat_pos = copy.deepcopy(new_pos)
        fish_num = eat_fish(eat_graph, eat_pos, sy, sx, sy+s_dy, sx+s_dx)
        back_tracking(eat_graph, eat_pos, eat_sum+fish_num)
        count += 1
        s_dy = ts_dy * count
        s_dx = ts_dx * count
        flag = False
    if flag:
        answer = max(answer, eat_sum)


graph = [[[0, 0] for _ in range(4)] for _ in range(4)]
pos = [[] for _ in range(17)]
for y in range(4):
    temp = list(map(int, input().split()))
    for x in range(4):
        graph[y][x] = [temp[2*x], temp[2*x+1]-1]
        pos[temp[2*x]] = [y, x]
answer = graph[0][0][0]
# 처음 상어한테 먹히기
pos[graph[0][0][0]] = [-1, -1]
graph[0][0][0] = -1
pos[0] = [0, 0]
back_tracking(graph, pos, answer)
print(answer)