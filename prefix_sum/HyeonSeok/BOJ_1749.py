import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    graph[i+1] = [0] + temp
tg = [g[:] for g in graph]

answer = -sys.maxsize
for y in range(1, N+1):
    for x in range(1, M+1):
        prefix_sum = 0
        for y_ in range(1, y+1):
            for x_ in range(1, x+1):
                prefix_sum += graph[y_][x_]
        tg[y][x] = prefix_sum   # 누적합 구해서 저장
        # 어차피 좌->우, 상->하 순이므로 바로 크기계산 해도 문제없음
        for y_ in range(1, y+1):
            for x_ in range(1, x+1):
                answer = max(answer, prefix_sum - tg[y_-1][x] - tg[y][x_-1] + tg[y_-1][x_-1])
print(answer)