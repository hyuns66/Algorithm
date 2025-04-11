def move(graph, pos, favorite_dir, shark_dir, area, smell):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(1, len(pos)):
        y, x = pos[i]
        # 이탈한 상어 제외
        if y == -1 or x == -1:
            continue
        idx = i-1
        ty, tx = -1, -1
        # 우선순위 방향순서로 빈칸 탐색
        for dir_idx in favorite_dir[idx][shark_dir[idx]]:
            dy, dx = dirs[dir_idx]
            # 우선순위 가장 높은 냄새없는 공간 찾으면 break
            if y+dy < 0 or x+dx < 0 or y+dy >= len(graph) or x+dx >= len(graph):
                continue
            if smell[y+dy][x+dx] == 0:
                ty = y+dy
                tx = x+dx
                break
        # 우선순위 방향순서로 본인 영역 탐색 (빈칸탐색 실패했을 시)
        if ty == -1 and tx == -1:
            for dir_idx in favorite_dir[idx][shark_dir[idx]]:
                dy, dx = dirs[dir_idx]
                if y+dy < 0 or x+dx < 0 or y+dy >= len(graph) or x+dx >= len(graph):
                    continue
                if area[y+dy][x+dx] == i:
                    ty = y+dy
                    tx = x+dx
                    break
        if ty == -1 and tx == -1:
            print("이동에러")
            exit(-1)
        # 이미 우선순위가 높은 상어가 들어와있으면 본인퇴장
        if graph[ty][tx] != 0:
            pos[i] = [-1, -1]
            graph[y][x] = 0
            continue
        else:
        # 아니면 해당자리로 이동
            pos[i] = [ty, tx]
            graph[y][x] = 0
            graph[ty][tx] = i
            shark_dir[idx] = dir_idx

def decrease_smell(smell, area):
    for y in range(len(smell)):
        for x in range(len(smell)):
            if smell[y][x] > 0:
                smell[y][x] -= 1
            if smell[y][x] == 0:
                area[y][x] = 0

def make_smell(graph, smell, area, pos):
    global k
    for shark_num in range(1, len(pos)):
        idx = shark_num - 1
        y, x = pos[shark_num]
        if y == -1 or x == -1:
            continue
        smell[y][x] = k
        area[y][x] = shark_num

def check(pos):
    count = 0
    for i in range(1, len(pos)):
        y, x = pos[i]
        if y != -1 and x != -1:
            count += 1
    if count == 1:
        return True
    else: 
        return False

N, M, k = map(int, input().split())
graph = list()
smell = [[0 for _ in range(N)] for _ in range(N)]   # 냄새 크기
area = [[-1 for _ in range(N)] for _ in range(N)]    # 냄새 주인
pos = [[0, 0] for _ in range(M+1)]
shark_dir = list()
favorite_dir = list()
for y in range(N):
    temp = list(map(int, input().split()))
    for x in range(N):
        if temp[x] != 0:
            pos[temp[x]] = [y, x]
            smell[y][x] = k
            area[y][x] = temp[x]
    graph.append(temp)
shark_dir = [int(x) - 1 for x in input().split()]
for i in range(M):
    temp = list()
    temp.append([int(x) - 1 for x in input().split()])
    temp.append([int(x) - 1 for x in input().split()])
    temp.append([int(x) - 1 for x in input().split()])
    temp.append([int(x) - 1 for x in input().split()])
    favorite_dir.append(temp)

answer = 0
while answer < 1000:
    move(graph, pos, favorite_dir, shark_dir, area, smell)
    decrease_smell(smell, area)
    make_smell(graph, smell, area, pos)
    answer += 1
    if check(pos):
        print(answer)
        exit(0)
print(-1)