import sys

N, d, k, c = map(int, sys.stdin.readline().split())
sushi = list()
sushi_set = set()
for _ in range(N):
    su = int(sys.stdin.readline())
    sushi.append(su)
    sushi_set.add(su)

answer = 0

# 순서대로 먹어서 보너스까지 받은경우 최대 가짓수
for idx in range(N-1, -1, -1):
    temp_set = set()
    for i in range(idx, idx-k, -1):
        su = sushi[i]
        temp_set.add(su)
    temp_set.add(c)
    answer = max(len(temp_set), answer)
    
# 보너스 못받은 경우 최대 가짓수
# temp = min(len(sushi_set), k)
# 최종
# answer = max(temp, answer)
print(answer)