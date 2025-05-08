def can_down(graph, gy, gx):
    if gy == len(graph) - 2:
        return False
    if graph[gy+2][gx] == 0 and graph[gy+1][gx-1] == 0 and graph[gy+1][gx+1] == 0:
        return True
    else:
        return False

def can_rotate_left(graph, gy, gx):
    if gy == len(graph) - 2:
        return False
    if gx == 1:
        return False
    if graph[gy][gx-2] == 0 and graph[gy-1][gx-1] == 0 and graph[gy+1][gx-1] == 0 and graph[gy+1][gx-2] == 0 and graph[gy+2][gx-1] == 0:
        return True
    else:
        return False

def can_rotate_right(graph, gy, gx):
    if gy == len(graph) - 2:
        return False
    if gx == len(graph[0]) - 2:
        return False
    if graph[gy][gx+2] == 0 and graph[gy-1][gx+1] == 0 and graph[gy+1][gx+1] == 0 and graph[gy+1][gx+2] == 0 and graph[gy+2][gx+1] == 0:
        return True
    else:
        False

def golem_down(graph, gy, gx):
    return gy+1, gx

def golem_rotate_left(graph, gy, gx, gdir):
    return gy+1, gx-1, (gdir+3)%4

def golem_rotate_right(graph, gy, gx, gdir):
    return gy+1, gx+1, (gdir+1)%4

def add_golem_to_map(graph, gy, gx, gdir, golem_num):
    global exit_dirs, is_exit
    graph[gy][gx] = golem_num
    graph[gy+1][gx] = golem_num
    graph[gy-1][gx] = golem_num
    graph[gy][gx+1] = golem_num
    graph[gy][gx-1] = golem_num
    gdy, gdx = exit_dirs[gdir]
    is_exit[gy+gdy][gx+gdx] = True

def fairy_dfs(graph, fy, fx, golem_num):
    global is_exit
    stack = list()
    answer = 0
    visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    visited[fy][fx] = True
    stack.append((fy, fx, golem_num))
    while stack:
        y, x, n = stack.pop()
        answer = max(y-2, answer)   # 최대 깊이 저장하는데 그래프가 3만큼 더 높은거 감안해서 적용
        for dy, dx in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            py, px = (y+dy, x+dx)
            if py < 0 or px < 0 or py >= len(graph) or px >= len(graph[0]):
                continue
            if visited[py][px] or graph[py][px] == 0:
                continue
            # 다른골렘 탑승할때는 출구인지 체크
            if graph[py][px] != n and not is_exit[y][x]:
                continue
            visited[py][px] = True
            stack.append((py, px, graph[py][px]))
    print(answer)
    return answer

R, C, K = map(int, input().split())
graph = [[0 for _ in range(C)] for _ in range(R+3)] # 위에서부터 내려오는거 구현하기 위해 여백을 줌 (최종 정답 구할때 3만큼 빼줘야함)
exit_dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
is_exit = [[False for _ in range(C)] for _ in range(R+3)]
golem_num = 1
answer = 0

for _ in range(K):
    ci, di = map(int, input().split())
    y = 1
    x = ci-1
    while True:
        if can_down(graph, y, x):
            y, x = golem_down(graph, y, x)
        elif can_rotate_left(graph, y, x):
            y, x, di = golem_rotate_left(graph, y, x, di)
        elif can_rotate_right(graph, y, x):
            y, x, di = golem_rotate_right(graph, y, x, di)
        else:
            break
    # 골렘이 위에 끼어 있으면 그래프 초기화 후 다음 골렘으로
    if y < 4:
        graph = [[0 for _ in range(C)] for _ in range(R+3)] # 위에서부터 내려오는거 구현하기 위해 여백을 줌 (최종 정답 구할때 3만큼 빼줘야함)
        is_exit = [[False for _ in range(C)] for _ in range(R+3)]
        golem_num = 1
        continue
    # 골렘정보 그래프에 추가 후 골렘 숫자 증가
    add_golem_to_map(graph, y, x, di, golem_num)
    answer += fairy_dfs(graph, y, x, golem_num)
    print("---------")
    for g in graph:
        print(g)
    for e in is_exit:
        print(e)
    golem_num += 1
print(answer)