def move(graph, clouds, dy, dx, si, N, visited):
    dy = dy*si
    dx = dx*si
    target = list()
    for y, x in clouds:
        graph[(y+dy)%N][(x+dx)%N] += 1
        target.append(((y+dy)%N, (x+dx)%N))
        visited[(y+dy)%N][(x+dx)%N]  = True
    return target

def bug(graph, target):
    for y, x in target:
        count = 0
        for dy, dx in [[1, 1], [1, -1], [-1, -1], [-1, 1]]:
            py, px = (y + dy, x + dx)
            if py < 0 or px < 0 or py >= N or px >= N:
                continue
            if graph[py][px] > 0:
                count += 1
        graph[y][x] += count

def make_cloud(graph, visited):
    clouds = list()
    for y in range(len(graph)):
        for x in range(len(graph)):
            if visited[y][x]:
                continue
            if graph[y][x] >= 2:
                graph[y][x] -= 2
                clouds.append((y, x))
    return clouds


N, M = map(int, input().split())
graph = list()
dirs = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]
for _ in range(N):
    graph.append(list(map(int, input().split())))
for _ in range(M):
    di, si = map(int, input().split())
    visited = [[False for _ in range(N)] for _ in range(N)]
    target = move(graph, clouds, dirs[di-1][0], dirs[di-1][1], si, N, visited)
    bug(graph, target)
    clouds = make_cloud(graph, visited)
print(sum(sum(graph[i]) for i in range(N)))