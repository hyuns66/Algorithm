import sys
"""
DFS (시간초과)
"""
# N = int(sys.stdin.readline())
# graph = list()
# for _ in range(N):
#     graph.append(list(map(int, sys.stdin.readline().split())))
# stack = list()
# answer = 0
# stack.append((0, 0))
# while stack:
#     y, x = stack.pop()
#     dist = graph[y][x]
#     if y == N-1 and x == N-1:
#         answer += 1
#         continue
#     for dir in [(1, 0), (0, 1)]:
#         tar_y, tar_x = y + (dist * dir[0]), x + (dist * dir[1])
#         if tar_y >= N or tar_x >= N:
#             continue
#         stack.append((tar_y, tar_x))
# print(answer)

"""
DP (정해)
"""
N = int(sys.stdin.readline())
graph = list()
dp = [[0 for i in range(N)] for j in range(N)]
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))
dp[0][0] = 1
for y in range(N):
    for x in range(N):
        if y == N-1 and x == N-1:
            continue
        dist = graph[y][x]
        for dir in [(1, 0), (0, 1)]:
            tar_y, tar_x = y + (dist * dir[0]), x + (dist * dir[1])
            if tar_y >= N or tar_x >= N:
                continue
            dp[tar_y][tar_x] += dp[y][x]
print(dp[-1][-1])