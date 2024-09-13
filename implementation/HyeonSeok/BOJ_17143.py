def catch_shark(graph, x):
    for y in range(len(graph)):
        if len(graph[y][x]) == 3:
            s, d, z = graph[y][x]
            graph[y][x].clear()
            return z
    return 0
        
def move_shark(graph, dir):
    new_graph = [[[] for _ in range(C)] for _ in range(R)]
    for y in range(len(graph)):
        for x in range(len(graph[0])):
            if len(graph[y][x]) == 0:
                continue
            s, d, z = graph[y][x]
            dy, dx = dir[d]
            py = y
            px = x
            for _ in range(s):
                if py+dy < 0 or py+dy >= len(graph) or px+dx < 0 or px+dx >= len(graph[0]):
                    dy = -dy
                    dx = -dx
                    d = d+1 if d==0 or d==2 else d-1
                py += dy
                px += dx
            if len(new_graph[py][px]) == 3:
                if new_graph[py][px][2] > z:
                    continue
                else:
                    new_graph[py][px] = [s, d, z]
            else:
                new_graph[py][px] = [s, d, z]
    return new_graph

R, C, M = map(int, input().split())
graph = [[[] for _ in range(C)] for _ in range(R)]
sharks = list()
dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
fish_king = -1
for _ in range(M):
    y, x, s, d, z = map(int, input().split())
    graph[y-1][x-1] = [s, d-1, z]
answer = 0
while fish_king < C-1:
    fish_king += 1
    answer += catch_shark(graph, fish_king)
    graph = move_shark(graph, dir)
print(answer)