import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [sys.maxsize for i in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(i+1, N):
        required_power = max(dp[i], (j - i) * (1 + abs(num_list[i] - num_list[j])))     # 이미 i번째 돌에서 100만큼의 힘이 필요한데 그다음 돌까지 가는데 1만큼의 힘만 필요하다면 필요한 힘은 어차피 100
        dp[j] = min(dp[j], required_power)  # i번째 돌에서 j번째 돌로 건너갈 때 필요한 힘을 최소값으로 업데이트 (이미 더 적은 힘으로 도달할 수 있는 상태면 업데이트가 일어나지 않음)
print(dp[-1])
