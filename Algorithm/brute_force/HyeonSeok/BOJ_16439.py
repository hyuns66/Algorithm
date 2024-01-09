import sys

N, M = map(int, sys.stdin.readline().split())
favorites = [[0 for j in range(M)] for i in range(N)]
chickens = list()
answer = 0

for i in range(N):
    f = list(map(int, sys.stdin.readline().split()))
    for k in range(M):
        favorites[i][k] = (f[k], k+1)
    favorites[i].sort(key=lambda x: (x[0], x[1]), reverse=True)

# 치킨 만족도 초기화
for i in range(M):
    chickens.append((i+1,))
    for j in range(i+1, M):
        chickens.append((i+1, j+1))
        for k in range(j+1, M):
            chickens.append((i+1, j+1, k+1))

# 치킨 만족도 업데이트
for chicken in chickens:
    temp = 0
    for f in favorites:
        for i in range(M):
            if f[i][1] in chicken:
                temp += f[i][0]
                break
    if temp > answer:
        answer = temp

print(answer)
