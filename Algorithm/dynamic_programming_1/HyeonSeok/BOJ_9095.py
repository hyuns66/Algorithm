import sys

answer = list()
T = int(sys.stdin.readline())
# 각 테스트 케이스에 대해 시행
for _ in range(T):
    n = int(sys.stdin.readline())
    dp = [0] * n
    for i in range(n):
        if i+1 <= 3:
            dp[i] = 1
        for j in range(1, 4):
            if i-j >= 0:
                dp[i] += dp[i-j]
    answer.append(dp[-1])

# 각 테스트 케이스에 대한 정답 출력
for a in answer:
    print(a)