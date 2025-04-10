def rotate(graph, py, px, n):
    temp = list()
    for i in range(n):
        temp.append(graph[py+i][px:px+n])
    for y in range(n):
        for x in range(n):
            graph[py+y][px+x] = temp[n-x-1][y]

def remove_ice(graph):
    remove_list = list()
    for y in range(len(graph)):
        for x in range(len(graph)):
            if graph[y][x] == 0:
                continue
            count = 0
            for dy, dx in [[1, 0], [0, -1], [0, 1], [-1, 0]]:
                py, px = (y+dy, x+dx)
                if py < 0 or px < 0 or py >= len(graph) or px >= len(graph):
                    continue
                if graph[py][px] > 0:
                    count += 1
            if count < 3:
                remove_list.append((y, x))
    for y, x in remove_list:
        graph[y][x] -= 1

def dfs(graph, visited, y, x):
    visited[y][x] = True
    stack = [(y, x)]
    count = 0
    while stack:
        py, px = stack.pop()
        count += 1
        for dy, dx in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            ty, tx = (py + dy, px + dx)
            if ty < 0 or tx  < 0 or ty >= len(graph) or tx >= len(graph):
                continue
            if graph[ty][tx] <= 0:
                continue
            if not visited[ty][tx]:
                visited[ty][tx] = True
                stack.append((ty, tx))
    return count

N, Q = map(int, input().split())
graph = list()
for _ in range(2**N):
    graph.append(list(map(int, input().split())))
query = list(map(int, input().split()))
for i in query:
    for y in range(0, 2**N, 2**i):
        for x in range(0, 2**N, 2**i):
            rotate(graph, y, x, 2**i)
    remove_ice(graph)


sum = sum(sum(graph[i]) for i in range(len(graph)))
print(sum)

answer = 0
visited = [[False for _ in range(len(graph))] for _ in range(len(graph))]
for y in range(len(graph)):
    for x in range(len(graph)):
        if visited[y][x]: continue
        if graph[y][x] <= 0: continue
        answer = max(answer, dfs(graph, visited, y, x))

print(answer)
