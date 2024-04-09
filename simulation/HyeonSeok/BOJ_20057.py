# dir_idx가 향하려고 하는 방향의 반시계 방향을 보고 아직 방문하지 않았으면
# turn이 가능하다고 알리기 위해 True를 반환하는 함수
# 회오리는 turn이 가능할 때 마다 turn 하는 방식으로 진행함.
def can_turn(visited, direction, dir_idx):
    return not visited[y+direction[(dir_idx+1)%4][0]][x+direction[(dir_idx+1)%4][1]]

def sand_storm(graph, y, x, dir):
    global N
    dy, dx = dir
    out_sand = 0
    dust = graph[y][x]
    dust_xs = int(0.01*dust)
    dust_s = int(0.02*dust)
    dust_m = int(0.05*dust)
    dust_l = int(0.07*dust)
    dust_xl = int(0.1*dust)
    dust_alpha = dust - 2*dust_xs - 2*dust_s - dust_m - 2*dust_l - 2*dust_xl
    if y+dx >= 0 and y+dx < N and x+dy >= 0 and x+dy < N:
        graph[y+dx][x+dy] += dust_l
    else:
        out_sand += dust_l
    if y-dx >= 0 and y-dx < N and x-dy >= 0 and x-dy < N:
        graph[y-dx][x-dy] += dust_l
    else:
        out_sand += dust_l
    if y+2*dx >= 0 and y+2*dx < N and x+2*dy >= 0 and x+2*dy < N:
        graph[y+2*dx][x+2*dy] += dust_s
    else:
        out_sand += dust_s
    if y-2*dx >= 0 and y-2*dx < N and x-2*dy >= 0 and x-2*dy < N:
        graph[y-2*dx][x-2*dy] += dust_s
    else:
        out_sand += dust_s
    if y-dy+dx >= 0 and y-dy+dx < N and x-dx+dy >= 0 and x-dx+dy < N:
        graph[y-dy+dx][x-dx+dy] += dust_xs
    else:
        out_sand += dust_xs
    if y-dy-dx >= 0 and y-dy-dx < N and x-dx-dy >= 0 and x-dx-dy < N:
        graph[y-dy-dx][x-dx-dy] += dust_xs
    else:
        out_sand += dust_xs
    if y+dy+dx >= 0 and y+dy+dx < N and x+dx+dy >= 0 and x+dx+dy < N:
        graph[y+dy+dx][x+dx+dy] += dust_xl
    else:
        out_sand += dust_xl
    if y+dy-dx >= 0 and y+dy-dx < N and x+dx-dy >= 0 and x+dx-dy < N:
        graph[y+dy-dx][x+dx-dy] += dust_xl
    else:
        out_sand += dust_xl
    if y+2*dy >= 0 and y+2*dy < N and x+2*dx >= 0 and x+2*dx < N:
        graph[y+2*dy][x+2*dx] += dust_m
    else:
        out_sand += dust_m
    if y+dy >= 0 and y+dy < N and x+dx >= 0 and x+dx < N:
        graph[y+dy][x+dx] += dust_alpha
    else:
        out_sand += dust_alpha
    graph[y][x] = 0
    return out_sand

N = int(input())
graph = list()
visited = [[False for _ in range(N)] for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]

answer = 0
y, x = N // 2, N // 2
dir_idx = 3
while y != 0 or x != 0:
    visited[y][x] = True
    if can_turn(visited, direction, dir_idx):
        dir_idx = (dir_idx + 1) % 4
    y, x = y + direction[dir_idx][0], x + direction[dir_idx][1]
    answer += sand_storm(graph, y, x, direction[dir_idx])
    
print(answer)