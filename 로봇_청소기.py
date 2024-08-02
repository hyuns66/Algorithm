# 0 : 노청소 1 : 벽 2: 청소
def clean(y, x, graph):
    if graph[y][x] == 0:
        graph[y][x] = 2

def can_clean(y, x, graph):
    for dy, dx in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        py = y+dy
        px = x+dx
        # if py < 0 or py >= len(graph) or px < 0 or px >= len(graph):
        #     continue
        if graph[py][px] == 0:
            return True
    return False

def can_goback(y, x, dir, graph):
    py = y-dir[0]
    px = x-dir[1]
    if graph[py][px] == 1:
        return False
    return True

# 청소 가능한 위치로 전진 후 위치 반환
def forward_clean(y, x, dir, graph):
    # 반시계 방향 회전
    temp = dir[0]
    dir[0] = -dir[1]
    dir[1] = temp
    dy = y+dir[0]
    dx = x+dir[1]
    if graph[dy][dx] == 0:
        return dy, dx
    else:
        return y, x
    
N, M = map(int, input().split())
y, x, dir_idx = map(int, input().split())
dir_map = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dir = dir_map[dir_idx]
graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))

while True:
    clean(y, x, graph)
    if not can_clean(y, x, graph):
        if can_goback(y, x, dir, graph):    # 후진할 수 있다면
            # 방향 유지한 채로 후진 후 1번으로
            y -= dir[0]
            x -= dir[1]
            continue
        else:   # 후진할 수 없다면 작동 중지
            break
    else:
        y, x = forward_clean(y, x, dir, graph)
        continue
    
answer = 0
for g in graph:
    for tile in g:
        if tile == 2:
            answer += 1
print(answer)
