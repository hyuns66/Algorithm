from collections import deque

N = int(input())
K = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]   # 빈공간
for _ in range(K):
    y, x = map(int, input().split())
    graph[y-1][x-1] = 1     # 사과
graph[0][0] = 2  # 뱀

L = int(input())
test_case = deque()
for _ in range(L):
    tc = list(input().split())
    tc[0] = int(tc[0])
    test_case.append(tc)
    
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0
diry, dirx = direction[dir_idx][0], direction[dir_idx][1]   # 전진 방향
posy, posx = 0, 0
body = deque()  # 몸 위치 기록해서 저장
body.append([0, 0])
time, dir_flag = test_case.popleft()
answer = 0
while True:
    answer += 1
    posy, posx = posy + diry, posx + dirx     # 전진 목적지
    if posy >= N or posy < 0 or posx >= N or posx < 0 or graph[posy][posx] == 2:  # 게임오버
        print(answer)
        break
    if graph[posy][posx] == 0:    # 빈공간 전진 시 꼬리 따라오기
        taily, tailx = body.popleft()
        graph[taily][tailx] = 0
    graph[posy][posx] = 2     # 사과 먹은 경우 머리만 전진
    body.append([posy, posx])
    if time == answer:
        if dir_flag == 'D':
            dir_idx = (dir_idx + 1) % 4
        else:
            dir_idx = (dir_idx + 3) % 4
        diry, dirx = direction[dir_idx][0], direction[dir_idx][1]   # 전진방향 업데이트
        if test_case:
            time, dir_flag = test_case.popleft()

