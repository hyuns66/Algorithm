import sys

def DFS(depth):
    global graph, N, M, answer
    if depth == N * M:
        answer += 1
        return
    y = depth // M
    x = depth % M
    if graph[y-1][x]==0 or graph[y][x-1]==0 or graph[y-1][x-1]==0:
        graph[y][x] = 1
        DFS(depth+1)
        graph[y][x] = 0
    DFS(depth+1)


N, M = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
answer = 0
DFS(0)
print(answer)