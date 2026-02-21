import sys

def backTracking(node, cost):
    global N, visited, graph, answer
    flag = True
    for i in range(N):
        if i == node:
            continue
        if not visited[i]:
            flag = False
            if graph[node][i] != 0:
                visited[i] = True
                backTracking(i, cost + graph[node][i])
                visited[i] = False
    if flag and graph[node][0] != 0:
        answer = min(answer, cost+graph[node][0])
        
N = int(sys.stdin.readline())
graph = list()
answer = sys.maxsize
visited = [False for _ in range(N)]
visited[0] = True   # 0번째 노드를 작작점으로 (어차피 순회이기 때문에 시작점을 어디로 잡던 상관없음)
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)

backTracking(0, 0)
print(answer)