import sys
from collections import deque

def BFS():
    global graph
    cost = 0
    visited = [[False for i in range(M)] for j in range(N)]
    broken_visited = [[False for a in range(M)] for b in range(N)]
    q = list()
    q.append((0, 0, False))
    visited[0][0] = True
    while q:
        current_q = deque(q[:])
        q.clear()
        cost += 1
        while current_q:
            y, x, is_broken = current_q.popleft()
            if y == N-1 and x == M-1:
                return cost
            # if not visited[y][x] and not is_broken:
            #     visited[y][x] = True
            for dy, dx in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= y + dy < N and 0 <= x + dx < M:
                    if is_broken:
                        if graph[y + dy][x + dx] == '0' and not broken_visited[y + dy][x + dx]:
                            q.append((y + dy, x + dx, is_broken))
                            broken_visited[y+dy][x+dx] = True
                    else:
                        if graph[y + dy][x + dx] == '0' and not visited[y+dy][x+dx]:
                            q.append((y + dy, x + dx, is_broken))
                            visited[y+dy][x+dx] = True
                        elif graph[y + dy][x + dx] == '1' and not is_broken:
                            q.append((y + dy, x + dx, True))
    return sys.maxsize

N, M = map(int, sys.stdin.readline().split())
graph = list()
walls = list()

for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

answer = BFS()

print(-1 if answer == sys.maxsize else answer)
