import sys

def dfs(pos_y, pos_x):
    global visited, n, m, graph
    stack = list()
    stack.append((pos_y, pos_x))
    visited[pos_y][pos_x] = True
    size = 0
    while stack:
        y, x = stack.pop()
        size += 1
        for dir in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            dir_y = y + dir[0]
            dir_x = x + dir[1]
            if dir_y >= n or dir_x >= m or dir_y < 0 or dir_x < 0:
                continue
            if graph[dir_y][dir_x] == 1 and not visited[dir_y][dir_x]:
                stack.append((dir_y, dir_x))
                visited[dir_y][dir_x] = True
    return size

n, m = map(int, sys.stdin.readline().split())
graph = list()
visited = [[False for _ in range(m)] for _ in range(n)]
max_size = 0
num = 0

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
    
for y in range(n):
    for x in range(m):
        if graph[y][x] == 1 and not visited[y][x]:
            num += 1
            max_size = max(max_size, dfs(y, x))

print(num)
print(max_size)