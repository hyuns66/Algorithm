import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

max_cnt = 0
dp = [[1, -1] for _ in range(N)]
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            if dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = j
answer = 0
start_idx = 0
answer_lis = []
for idx, info in enumerate(dp):
    count = info[0]
    if count > answer:
        answer = count
        start_idx = idx
while True:
    answer_lis.append(A[start_idx])
    start_idx = dp[start_idx][1]
    if start_idx == -1:
        break
answer_lis.reverse()
print(answer)
print(*answer_lis)