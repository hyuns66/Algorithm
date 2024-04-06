import sys

M, N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = list()
graph.append([[0, 0, 0] for _ in range(N+1)])
query = list()
for _ in range(M):
    temp = list(sys.stdin.readline().rstrip())
    for idx, t in enumerate(temp):
        if t == 'J':
            temp[idx] = [1, 0, 0]
        if t == 'O':
            temp[idx] = [0, 1, 0]
        if t == 'I':
            temp[idx] = [0, 0, 1]
    graph.append([[0, 0, 0]] + temp)
for _ in range(K):
    temp = list(map(int, sys.stdin.readline().split()))
    query.append(temp)
    
for y in range(1, M+1):
    for x in range(1, N+1):
        left = graph[y][x-1]
        top = graph[y-1][x]
        cross = graph[y-1][x-1]
        sum_list = [x+y for x,y in zip(left, top)]
        sub_list = [x-y for x,y in zip(sum_list, cross)]
        graph[y][x] = [x+y for x,y in zip(sub_list, graph[y][x])]


for sy, sx, ey, ex in query:
    left = graph[ey][sx-1]
    top = graph[sy-1][ex]
    cross = graph[sy-1][sx-1]
    sum_list = [x+y for x,y in zip(graph[ey][ex], cross)]
    sub_list = [x+y for x,y in zip(left, top)]
    answer = [x-y for x,y in zip(sum_list, sub_list)]
    print(*answer)
