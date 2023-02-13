import sys

N, M = map(int, sys.stdin.readline().split())    # 건물, 도로 수
inf = sys.maxsize
town = [[inf for j in range(N+1)] for i in range(N+1)]
answer = [1, 2, inf]

for i in range(1, N+1):
    town[i][i] = 0

# 데이터 입력받아서 town map 초기화 하기
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    town[a][b] = 1
    town[b][a] = 1

# Floyd-Warshall 로 town map 만들기
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            town[j][k] = min(town[j][k], town[j][i] + town[i][k])

# 치킨집 박아놓고 거리구하기
for i in range(1, N+1):
    for j in range(1, N+1):
        dist = 0
        for k in range(1, N+1):
            dist += min(town[k][i], town[k][j])
        if (2 * dist) < answer[2]:
            answer = [i, j, 2 * dist]

print(*answer)
