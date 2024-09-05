def check(graph):
    for start in range(len(graph[0])):
        y = 0
        end = start
        while y < len(graph):
            end += graph[y][end]
            y += 1
        if start != end:
            return False
    return True

def backTracking(graph, depth, start_idx, answer):
    if check(graph):
        return depth
    else:
        if depth == 3:
            return 4
    # start_idx의 정체 : 중복되는 케이스가 없도록 permutation을 구하기 위함. (depth가 증가하면서 다시 처음부터 탐색하지 않고 해당 인덱스 뒷부분만 이어서 탐색하도록 함)
    # 이거 안하면 시간초과 난다.
    for idx in range(start_idx+1, (len(graph[0])-1)*len(graph)):
        y = idx // (len(graph[0])-1)
        x = idx % (len(graph[0])-1)
        if graph[y][x] != 0 or graph[y][x+1] != 0:
            continue
        graph[y][x] = 1
        graph[y][x+1] = -1
        answer = min(answer, backTracking(graph, depth+1, idx, answer))
        graph[y][x] = 0
        graph[y][x+1] = 0
    return answer 

N, M, H = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[a-1][b] = -1

answer = backTracking(graph, 0, -1, 5)
if answer >= 4:
    answer = -1
print(answer)

