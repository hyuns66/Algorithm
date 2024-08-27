def check(graph):
    maxnum = 0
    for g in graph:
        for num in g:
            maxnum = max(num, maxnum)
    return maxnum

def move(original_graph, direction):
    order, dir = direction
    graph = [g[:] for g in original_graph]
    # 세로
    if order == 1:
        # 위
        if dir == 1:
            for x in range(len(graph)):
                new_column = list()
                temp = 0
                for y in range(len(graph)):
                    if graph[y][x] == 0:
                        continue
                    if graph[y][x] != temp:
                        temp = graph[y][x]
                        new_column.append(graph[y][x])
                    else:
                        temp = 0
                        new_column[-1] = new_column[-1]*2
                for y in range(len(graph)):
                    graph[y][x] = new_column[y] if y < len(new_column) else 0
        # 아래
        else:
            for x in range(len(graph)):
                new_column = list()
                temp = 0
                for y in range(len(graph)-1, -1,-1):
                    if graph[y][x] == 0:
                        continue
                    if graph[y][x] != temp:
                        temp = graph[y][x]
                        new_column.append(graph[y][x])
                    else:
                        temp = 0
                        new_column[-1] = new_column[-1]*2
                for y in range(len(graph)):
                    graph[-y-1][x] = new_column[y] if y < len(new_column) else 0
    # 가로
    else:
        if dir == 1:
            for y in range(len(graph)):
                new_row = list()
                temp = 0
                for x in range(len(graph)):
                    if graph[y][x] == 0:
                        continue
                    if graph[y][x] != temp:
                        temp = graph[y][x]
                        new_row.append(graph[y][x])
                    else:
                        new_row[-1] = new_row[-1]*2
                        temp = 0
                for x in range(len(graph)):
                    graph[y][x] = new_row[x] if x < len(new_row) else 0
        else:
            for y in range(len(graph)):
                new_row = list()
                temp = 0
                for x in range(len(graph)-1, -1, -1):
                    if graph[y][x] == 0:
                        continue
                    if graph[y][x] != temp:
                        temp = graph[y][x]
                        new_row.append(graph[y][x])
                    else:
                        new_row[-1] = new_row[-1]*2
                        temp = 0
                for x in range(len(graph)):
                    graph[y][-x-1] = new_row[x] if x < len(new_row) else 0
    return graph

def backtracking(graph, depth, answer):
    if depth == 5:
        answer = max(check(graph), answer)
        return answer
    for direction in [[1, 1], [-1, 1], [1, -1], [-1, -1]]:
        new_graph = move(graph, direction)
        answer = backtracking(new_graph, depth+1, answer)
    return answer
    
        
N = int(input())
graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))

print(backtracking(graph, 0, 0))