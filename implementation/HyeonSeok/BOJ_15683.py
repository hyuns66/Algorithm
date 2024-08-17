def rotate(cctv):
    directions = cctv
    for i in range(4):
        new_directions = list()
        for dir in directions:
            new_directions.append([dir[1], -dir[0]])
        directions = new_directions[:]
        yield new_directions

def backtracking(cctvs, graph, position, depth):
    if depth >= len(cctvs):
        return count(graph)
    y, x = position[depth]
    cctv = cctvs[depth]
    answer = 100
    for directions in rotate(cctv):
        # 주어진 cctv방향 감시 영역 마스킹
        for direction in directions:
            py = y + direction[0]
            px = x + direction[1]
            while py >= 0 and px >= 0 and py < len(graph) and px < len(graph[0]):
                if graph[py][px] == 6:
                    break
                if graph[py][px] <= 0:
                    graph[py][px] -= 1
                py += direction[0]
                px += direction[1]
        answer = min(answer, backtracking(cctvs, graph, position, depth+1))
        # 주어진 cctv방향 감시 영역 마스킹 취소
        for direction in directions:
            py = y + direction[0]
            px = x + direction[1]
            while py >= 0 and px >= 0 and py < len(graph) and px < len(graph[0]):
                if graph[py][px] == 6:
                    break
                if graph[py][px] < 0:
                    graph[py][px] += 1
                py += direction[0]
                px += direction[1]
    return answer

def count(graph):
    count = 0
    for g in graph:
        for num in g:
            if num == 0:
                count += 1
    return count

N, M = map(int, input().split())
graph = list()
cctv = [
    [[0, 1]], 
    [[0, 1], [0, -1]],
    [[0, 1], [-1, 0]],
    [[0, 1], [-1, 0], [0, -1]],
    [[0, 1], [-1, 0], [0, -1], [1, 0]]
    ]
for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = 0
cctvs = list()
position = list()
for y in range(N):
    for x in range(M):
        if graph[y][x] == 0 or graph[y][x] >= 6:
            continue
        cctvs.append(cctv[graph[y][x]-1])
        position.append((y, x))
print(backtracking(cctvs, graph, position, 0))

        