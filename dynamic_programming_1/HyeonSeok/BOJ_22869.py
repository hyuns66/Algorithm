import sys

N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [False] * N    # 갈 수 있는 돌이면 True 아니면 False
dp[0] = True    # 시작점 True로 초기화
# 처음부터 나아가면서 갈 수 있는 돌들에 체크하며 밟아나감
for i in range(N):
    if not dp[i]:   # 갈 수 없는 돌이면 고려하지 않음
        continue
    for dist in range(1, K+1):  # 현재위치에서 앞으로 갈 수 있는 돌들에 True 표시
        if i + dist < N and dist * (1 + abs(num_list[i] - num_list[i + dist])) <= K:
            dp[i + dist] = True
# 결과적으로 마지막 돌이 도달할 수 있는지만 체크
print('YES' if dp[-1] else 'NO')
