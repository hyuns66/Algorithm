def back_tracking(y, x, graph, num, fish_alive):     # 상어위치, 현재그래프, 먹은 물고기 합
    global answer
    diry, dirx = direction[graph[y][x][1]]
    # print(fish_alive)
    # for g in graph:
    #     print(g)
    graph = move_fishes([g[:] for g in graph], fish_alive)
    leave_flag = True
    for i in range(1, 4):
        tary, tarx = y + diry*i, x + dirx*i
        if tary < 0 or tary >= 4 or tarx < 0 or tarx >= 4:
            break
        if graph[tary][tarx][0] == 0:
            continue
        leave_flag = False
        temp = graph[tary][tarx]
        graph[tary][tarx] = [-1, temp[1]]      # 물고기 잡아먹은 후 해당 방향으로 업뎃
        graph[y][x][0] = 0
        fish_alive[temp[0]] = False
        back_tracking(tary, tarx, [g[:] for g in graph], num+temp[0], fish_alive[:])
        graph[tary][tarx] = temp
        fish_alive[temp[0]] = True
    if leave_flag:
        answer = max(num, answer)
    
# 한 턴에 물고기들이 모두 이동한 후 그래프 반환
def move_fishes(graph, fish_alive):
    for idx in range(1, 17):
        y, x = fish_position[idx]
        # 물고기가 이미 먹혀서 없는 상태면 skip
        if not fish_alive[idx]:
            continue
        # print(y, x, graph[y][x], idx, fish_alive)
        diry, dirx = direction[graph[y][x][1]]    # 물고기가 움직일 방향
        tary, tarx = y + diry, x + dirx # 물고기가 움직일 목적지
        while tary < 0 or tary >= 4 or tarx < 0 or tarx >= 4 or graph[tary][tarx][0] == -1:      # 막힌경우 반시계 방향으로 재설정
            new_dir_idx = graph[y][x][1] + 1 if graph[y][x][1] < 8 else 1
            diry, dirx = direction[new_dir_idx]
            tary, tarx = y + diry, x + dirx
            graph[y][x][1] = new_dir_idx
            # print(tary, tarx)
        # 물고기 이동 (자리바꾸기)
        temp = graph[tary][tarx]
        graph[tary][tarx] = graph[y][x]
        graph[y][x] = temp
        fish_position[idx] = [tary, tarx]
        fish_position[temp[0]] = [y, x]
    return graph
        
        
# -1 상어,  0 빈칸,  1~16 물고기
graph = list()
fish_position = [[] for _ in range(17)]     # 물고기 번호에 [y, x] 위치 저장
for y in range(4):
    temp = list(map(int, input().split()))
    g = list()
    for x in range(4):
        fish_position[temp[x*2]] = [y, x]
        g.append([temp[x*2], temp[x*2+1]])      # 물고기 번호, 방향
    graph.append(g)
    
answer = 0
direction = [0, [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
fish_alive = [True for _ in range(17)]
temp = graph[0][0][0]
graph[0][0][0] = -1
answer = temp
fish_alive[temp] = False

back_tracking(0, 0, [g[:] for g in graph], temp, fish_alive)
print(answer)
