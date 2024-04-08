import sys
from collections import deque
import heapq

# pos 지점으로 부터 graph상에 있는 모든 물고기에 대한 최단경로 구한다음 -> 그중 가장 가까운 물고기를 택한다.
# 이걸 물고기가 모두 사라질 때 까지 반복, BFS를 다 돌았는데 물고기가 존재하지 않는 경우 return
def bfs(pos):
    global N, graph, answer, exp, size, direction
    q = deque()
    q.append((pos[0], pos[1], 0))
    visited = [[False for i in range(N)] for j in range(N)]
    visited[pos[0]][pos[1]] = True
    fishes = []
    if exp >= size:
        size += 1
        exp = 0
    while q:
        y, x, walk = q.popleft()
        for d in direction:
            d_y = y+d[0]
            d_x = x+d[1]
            if 0 <= d_y < N and 0 <= d_x < N and graph[d_y][d_x] <= size and not visited[d_y][d_x]:
                visited[d_y][d_x] = True
                if 0 < graph[d_y][d_x] < size:
                    heapq.heappush(fishes, (walk+1, d_y, d_x))
                q.append((d_y, d_x, walk + 1))
    if fishes:
        walk, y, x = heapq.heappop(fishes)
        exp += 1
        answer += walk
        graph[y][x] = 0
        bfs((y,x))
    else:
        return

N = int(sys.stdin.readline())
direction = [[-1, 0], [0, -1], [0, 1], [1, 0]]
graph = []
answer = 0
exp = 0
size = 2
pos = [0, 0]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    if 9 in temp:
        pos = [i, temp.index(9)]
    graph.append(temp)

# 본인의 위치가 숫자 9로 초기화 되기 때문에 숫자로 표시되는 물고기의 크기와 혼동되지 않도록 시작좌표만 기록해두고 0으로 초기화해준다.
graph[pos[0]][pos[1]] = 0

bfs(pos)
print(answer)