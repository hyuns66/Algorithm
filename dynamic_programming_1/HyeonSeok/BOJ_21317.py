import sys

N = int(sys.stdin.readline())
jump_info = list()
for _ in range(N-1):
    little, middle = map(int, sys.stdin.readline().split())
    jump_info.append((little, middle))
K = int(sys.stdin.readline())
skip_dp = [[sys.maxsize for i in range(N)] for j in range(N-3)]
no_skip_dp = [sys.maxsize] * N
no_skip_dp[0] = 0
for i in range(N-1):
    no_skip_dp[i+1] = min(no_skip_dp[i+1], no_skip_dp[i] + jump_info[i][0])
    if i < N-2:
        no_skip_dp[i+2] = min(no_skip_dp[i+2], no_skip_dp[i] + jump_info[i][1])
for j in range(N-3):
    skip_dp[j][0] = 0
    skip_dp[j][j+1] = 0
    skip_dp[j][j+2] = 0
    for i in range(N-1):
        if i > 0 >= skip_dp[j][i]:
            continue
        skip_dp[j][i + 1] = min(skip_dp[j][i + 1], skip_dp[j][i] + jump_info[i][0])
        if i < N-2:
            skip_dp[j][i + 2] = min(skip_dp[j][i + 2], skip_dp[j][i] + jump_info[i][1])
        if i == j:
            skip_dp[j][j+3] = skip_dp[j][i] + K
answer = sys.maxsize
for d in skip_dp:
    answer = min(answer, d[-1])
answer = min(no_skip_dp[-1], answer)
# max_idx = 0
# max_value = 0
# for i in range(N-3):
#     max_value = dp[max_idx + 3] - dp[max_idx]
#     temp_value = dp[i + 3] - dp[i]
#     if temp_value > max_value:
#         max_value = temp_value
#         max_idx = i
# print(max_value)
# if max_value > K:
#     answer = answer - max_value + K
# print(dp)
print(answer)