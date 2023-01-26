import sys
from collections import deque

N, M, T = map(int, sys.stdin.readline().split())
graph = list()

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

q = deque()
q.append((0, 0, 0, False))
visited = [[False for i in range(M)] for j in range(N)]
visited[0][0] = True
answer = sys.maxsize
while q:
    y, x, cost, gram = q.popleft()
    if y == N-1 and x == M-1 and answer > cost:
        answer = cost
        continue
    if gram:
        temp = cost + N - y + M - x - 2
        if temp < answer:
            answer = temp
            continue
    for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        cur_y = y + dy
        cur_x = x + dx
        if not (0 <= cur_y < N) or not (0 <= cur_x < M) or visited[cur_y][cur_x]:
            continue
        if graph[cur_y][cur_x] == 0:
            q.append((cur_y, cur_x, cost + 1, False))
            visited[cur_y][cur_x] = True
        elif graph[cur_y][cur_x] == 2:
            q.append((cur_y, cur_x, cost + 1, True))
            visited[cur_y][cur_x] = True

print("Fail" if answer > T else answer)