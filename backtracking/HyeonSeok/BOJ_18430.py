import sys

def backTracking(depth, cost):
    global Y, X, visited, graph, answer
    dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    y = depth // X
    x = depth % X
    if depth == Y * X:
        answer = max(answer, cost)
        return
    for dir in dirs:
        dir_y = dir[0]
        dir_x = dir[1]
        if not visited[y+1][x+1] and not visited[y+1+dir_y][x+1] and not visited[y+1][x+1+dir_x]:
            visited[y+1+dir_y][x+1] = True
            visited[y+1][x+1+dir_x] = True
            visited[y+1][x+1] = True
            cur_cost = 2*graph[y][x] + graph[y+dir_y][x] + graph[y][x+dir_x]
            backTracking(depth+1, cost + cur_cost)
            visited[y+1+dir_y][x+1] = False
            visited[y+1][x+1+dir_x] = False
            visited[y+1][x+1] = False

    backTracking(depth+1, cost)



Y, X  = map(int, sys.stdin.readline().split())
graph = list()
visited = [[False for _ in range(X+2)] for _ in range(Y+2)]
answer = 0
for i in range(X+2):
    visited[0][i] = True
    visited[Y+1][i] = True
for i in range(Y+2):
    visited[i][0] = True
    visited[i][X+1] = True
for _ in range(Y):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
   
backTracking(0, 0)
print(answer)