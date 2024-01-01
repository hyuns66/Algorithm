# import sys

# def recursion(visited, node):
#     global dp, graph, N, answer
#     if visited == (1 << N) - 1:
#         if graph[node][0] != 0:
#             answer = min(answer, dp[node][visited] + graph[node][0])
#         return
#     for i in range(1, N):
#         if not visited & (1 << i) and graph[node][i] != 0:
#             if (visited | (1 << i)) not in dp[i]:
#                 dp[i][visited | (1 << i)] = dp[node][visited] + graph[node][i]
#             else:
#                 dp[i][visited | (1 << i)] = min(dp[i][visited | (1 << i)], dp[node][visited] + graph[node][i])
#             recursion(visited | (1 << i), i)

# N = int(sys.stdin.readline())
# graph = list()
# answer = sys.maxsize
# dp = [dict() for _ in range(N)]
# for _ in range(N):
#     temp = list(map(int, sys.stdin.readline().split()))
#     graph.append(temp)
# dp[0][1] = 0

# recursion(1, 0)

# print(answer)

import sys
N = int(input())
world = []
for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))

dp = {}


def DFS(now, visited):
    # 모든 도시를 방문한 경우
    if visited == (1 << N) - 1:
        # 다시 출발 도시로 갈 수 있는 경우 출발 도시까지의 비용 반환
        if world[now][0]:
            return world[now][0]
        else:
            # 갈 수 없는 경우 무한대 반환 (이 경로가 최소비용으로 채택되지 않게)
            return int(1e9)

    # 이전에 계산된 경우 결과 반환
    if (now, visited) in dp:
        return dp[(now, visited)] # now까지 방문한 최소 비용

    min_cost = int(1e9)
    for next in range(1, N):
        # 비용이 0이어서 갈 수 없거나, 이미 방문한 루트면 무시
        if world[now][next] == 0 or visited & (1 << next):
            continue
        cost = DFS(next, visited | (1 << next)) + world[now][next]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost  # 현재도시까지 방문한 경우 중에서 최소 비용이 드는 루트의 비용 저장
    print(dp)
    return min_cost  # 현재도시까지 방문하는 비용 리턴


print(DFS(0, 1))  # now: 0번째 도시부터 방문, visited: 0번째 도시 방문 처리