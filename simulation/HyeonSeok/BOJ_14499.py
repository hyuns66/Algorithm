"""
오른쪽 회전
  2            2
4 1 3   ->   6 4 1
  5            5
  6            3

왼쪽 회전
  4            4
6 5 1   ->   5 1 2
  3            3
  2            6

오른쪽 회전의 경우 row의 가장 우측이 col의 하단과 교환되며
왼쪽 회전의 경우 row의 가장 좌측이 col의 하단과 교환된 후 rotate되는 규칙 있음
deque로 구현.
주의 할 점 : row가 rotate 하게 되면 col도 영향을 받기 때문에 동기화 해주어야 한다. 반대도 마찬가지.
"""

from collections import deque

N, M, y, x, K = map(int, input().split())
graph = list()
for _ in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
order = list(map(int, input().split()))
direction = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]

# 주사위 전개도
col = deque([0, 0, 0, 0])
row = deque([0, 0, 0])

for o in order:
    dy, dx = direction[o]
    py, px = y + dy, x + dx
    # 밖으로 나가는 경우 무시
    if py >= N or py < 0 or px >= M or px < 0:
        continue
    else:
        y, x = py, px
    # 주사위 col 회전 후 row중심 동기화 해주기
    col.rotate(dy)
    row[1] = col[1]
    # 주사위 row 회전 후 col중심 동기화 해주기
    if dx == 1:
        temp = row[-1]
        row[-1] = col[-1]
        col[-1] = temp
        row.rotate(1)
    elif dx == -1:
        temp = row[0]
        row[0] = col[-1]
        col[-1] = temp
        row.rotate(-1)
    col[1] = row[1]
    # 주사위와 그래프 숫자 업데이트
    if graph[y][x] == 0:
        graph[y][x] = col[-1]
    else:
        col[-1] = graph[y][x]
        graph[y][x] = 0
    print(col[1])
    