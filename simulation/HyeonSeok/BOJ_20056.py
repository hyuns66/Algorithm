N, M, K = map(int, input().split())
id = 0
graph = [[set() for _ in range(N)] for _ in range(N)]
fireball = dict()       # y, x, 질량, 속력, 방향
for _ in range(M):
    f = list(map(int, input().split()))
    fireball[id] = f
    graph[f[0]-1][f[1]-1].add(id)  # 그래프에는 질량, 속력, 방향, 움직임 여부로 파이어볼 정보 저장
    id += 1
        
direction = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
for i in range(K):
    # 1.모든 파이어볼 이동
    new_graph = [[set() for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            for fb_id in list(graph[y][x]):
                posy, posx, m, s, d = fireball[fb_id]
                tary, tarx = y+(s*direction[d][0]), x+(s*direction[d][1])
                if tarx >= N:
                    tarx = tarx % N
                if tary >= N:
                    tary = tary % N
                if tarx < 0:
                    tarx = (N + tarx) % N
                if tary < 0:
                    tary = (N + tary) % N
                # 딕셔너리에서 파이어볼 정보 업데이트
                fireball[fb_id][0] = tary
                fireball[fb_id][1] = tarx
                # 그래프에서 파이어볼 이동
                new_graph[tary][tarx].add(fb_id)
    graph = new_graph
    # 2. 2개 이상의 파이어볼 존재하는 경우
    for y in range(N):
        for x in range(N):
            if len(graph[y][x]) <= 1:
                continue
            odd_cnt = 0
            even_cnt = 0
            m_sum = 0
            s_sum = 0
            for fb_id in list(graph[y][x]):
                # 파이어볼이 하나로 합쳐짐
                m_sum += fireball[fb_id][2]
                s_sum += fireball[fb_id][3]
                # 파이어볼 방향 홀짝 카운트 (분할 후 방향결정을 위함)
                if fireball[fb_id][4] & 1 == 0:
                    even_cnt += 1
                else:
                    odd_cnt += 1
            child_m = m_sum // 5     # 나눠진 파이어볼 질량
            child_s = s_sum // len(graph[y][x])     # 나눠진 파이어볼 속력
            dir = [0, 2, 4, 6] if even_cnt * odd_cnt == 0 else [1, 3, 5, 7]     # 나눠진 파이어볼 방향
            # 합쳐질 파이어볼 정보 삭제
            for key in graph[y][x]:
                del fireball[key]
            graph[y][x] = set()
            # 질량이 0인경우 소멸
            if child_m == 0:
                continue
            # 나눠질 파이어볼 정보 입력
            for i in range(4):
                graph[y][x].add(id)
                fireball[id] = [y, x, child_m, child_s, dir[i]]
                id += 1
                
answer = 0
for y in range(N):
    for x in range(N):
        for fb_id in list(graph[y][x]):
            answer += fireball[fb_id][2]
            
print(answer)