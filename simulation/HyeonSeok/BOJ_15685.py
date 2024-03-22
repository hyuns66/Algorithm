import sys
# 시계 방향 회전 규칙 : 방향벡터 기준 (x, y) -> (-y, x)

def generate_curve(seq):
    endy, endx = seq[-1]
    for i in range(len(seq)-2, -1, -1):
        vy, vx = seq[i][0]-endy, seq[i][1]-endx
        seq.append([endy+vx, endx-vy])

N = int(sys.stdin.readline())
graph = [[False for _ in range(101)] for _ in range(101)]
init_dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]

for _ in range(N):
    seq = list()
    x, y, d, g = map(int, sys.stdin.readline().split())
    seq.append([y, x])
    seq.append([y+init_dir[d][0], x+init_dir[d][1]])
    for i in range(1, g+1):
        generate_curve(seq)
    for y, x in seq:
        graph[y][x] = True

answer = 0
for y in range(100):
    for x in range(100):
        if graph[y][x] and graph[y][x+1] and graph[y+1][x] and graph[y+1][x+1]:
            answer += 1
print(answer)