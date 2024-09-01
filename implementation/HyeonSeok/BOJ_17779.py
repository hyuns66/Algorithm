def make_sectors(x, y, d1, d2, graph):
    line_map = [[0 for _ in range(len(graph))] for _ in range(len(graph))]
    for i in range(d1+1):
        line_map[y+i][x-i] = 5
        line_map[y+d2+i][x+d2-i] = 5
    for i in range(d2+1):
        line_map[y+i][x+i] = 5
        line_map[y+d1+i][x-d1+i] = 5
    for i in range(y+1, y+d1+d2):
        flag = False
        for j in range(len(graph)):
            if line_map[i][j] == 5:
                flag = not flag
            else:
                if flag:
                    line_map[i][j] = 5
    for r in range(len(graph)):
        for c in range(len(graph)):
            if line_map[r][c] == 5:
                continue
            if r < y+d1 and c <= x:
                line_map[r][c] = 1
            if r <= y+d2 and c > x:
                line_map[r][c] = 2
            if y+d1 <= r and c < x-d1+d2:
                line_map[r][c] = 3
            if y+d2 < r and x-d1+d2 <= c:
                line_map[r][c] = 4
    return count(graph, line_map)

def count(graph, line_map):
    count = [0, 0, 0, 0, 0]
    for y in range(len(graph)):
        for x in range(len(graph)):
            count[line_map[y][x]-1] += graph[y][x]
    return max(count) - min(count)    

N = int(input())
graph = list()
answer = 400000
for _ in range(N):
    graph.append(list(map(int, input().split())))
for y in range(N):
    for x in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if y+d1+d2 <= N-1 and 0 <= x-d1 < x < x+d2 <= N-1:
                    answer = min(answer, make_sectors(x, y, d1, d2, graph))
print(answer)