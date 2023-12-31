import sys

def recursion(visited, node):
    global dp, graph, N, answer
    print(dp)
    if visited == (1 << N) - 1:
        if graph[node][0] != 0:
            answer = min(answer, dp[node][visited] + graph[node][0])
        return
    if visited in dp[node] and node != 0:
        return
    for i in range(1, N):
        if not visited & (1 << i) and graph[node][i] != 0:
            if (visited | (1 << i)) not in dp[i]:
                dp[i][visited | (1 << i)] = dp[node][visited] + graph[node][i]
            else:
                dp[i][visited | (1 << i)] = min(dp[i][visited | (1 << i)], dp[node][visited] + graph[node][i])
            recursion(visited | (1 << i), i)

N = int(sys.stdin.readline())
graph = list()
answer = sys.maxsize
dp = [dict() for _ in range(N)]
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
dp[0][1] = 0

recursion(1, 0)

print(answer)