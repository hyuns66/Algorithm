import sys
from collections import deque
"""
BFS (메모리 초과)
"""
# N = int(sys.stdin.readline())
# graph = list()
# for _ in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))
#
# q = deque()
# start = 1 if graph[0][0] == 0 else 0
# q.append((0, 0, graph[0][0], start))
# answer = 0
# while q:
#     cur_y, cur_x, milk, cnt = q.popleft()
#     if cur_y == N-1 and cur_x == N-1:
#         answer = max(answer, cnt)
#     for dir in [(1, 0), (0, 1)]:
#         tar_y, tar_x = cur_y+dir[0], cur_x+dir[1]
#         if tar_y >= N or tar_x >= N:
#             continue
#         tar_milk = graph[tar_y][tar_x]
#         next_cnt = 1 if tar_milk == (milk+1)%3 else 0
#         q.append((tar_y, tar_x, tar_milk, cnt+next_cnt))
# print(answer)

"""
DFS(시간초과)
"""
# N = int(sys.stdin.readline())
# graph = list()
# for _ in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))
# # dp = [[0 for i in range(N)] for j in range(N)]
# stack = list()
# start = 1 if graph[0][0] == 0 else 0
# stack.append((0, 0, graph[0][0], start))
# answer = 0
# while stack:
#     cur_y, cur_x, milk, cnt = stack.pop()
#     if cur_y == N - 1 and cur_x == N - 1:
#         answer = max(answer, cnt)
#     for dir in [(1, 0), (0, 1)]:
#         tar_y, tar_x = cur_y + dir[0], cur_x + dir[1]
#         if tar_y >= N or tar_x >= N:
#             continue
#         tar_milk = graph[tar_y][tar_x]
#         next_cnt = 1 if tar_milk == (milk+1)%3 else 0
#         stack.append((tar_y, tar_x, tar_milk, cnt+next_cnt))
# print(answer)
"""
DP(정해)
"""
N = int(sys.stdin.readline())
graph = list()
for i in range(N+1):
    if i == 0:
        graph.append([0 for j in range(N+1)])
    else:
        temp = [0]
        temp.extend(list(map(int, sys.stdin.readline().split())))
        graph.append(temp)
dp = [[[0 for i in range(3)] for j in range(N+1)] for k in range(N+1)]
for y in range(1, N+1):
    for x in range(1, N+1):
        for dir in [(-1, 0), (0, -1)]:
            tar_y, tar_x = y+dir[0], x+dir[1]
            cur_milk = graph[y][x]
            for i in range(3):
                if cur_milk == (i+1) % 3:
                    dp[y][x][i] = max(dp[y][x][i], dp[tar_y][tar_x][2-i] + 1)
                else:
                    dp[y][x][i] = max(dp[tar_y][tar_x][i], dp[y][x][i])
# for i in range(N+1):
#     for j in range(N+1):
#         print(dp[i][j][0])
print(max(dp[N][N][0], dp[N][N][1], dp[N][N][2]))