import sys

T = int(sys.stdin.readline())
answer = list()
for _ in range(T):
    N = int(sys.stdin.readline())
    sticker = list()
    for idx in range(2):
        temp = list(map(int, sys.stdin.readline().split()))
        sticker.append(temp)
    dp = [[0 for i in range(N)] for j in range(2)]
    if N == 1:
        answer.append(max(sticker[0][0], sticker[1][0]))
        continue
    elif N == 2:
        answer.append(max(sticker[0][0]+sticker[1][1], sticker[1][0]+sticker[0][1]))
        continue
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[1][0] + sticker[0][1]
    dp[1][1] = sticker[1][1] + sticker[0][0]
    for i in range(2, N):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]
    answer.append(max(dp[0][N-1], dp[1][N-1]))

for a in answer:
    print(a)
"""
최적화 코드
"""
# import sys
# input=sys.stdin.readline
#
#
# if __name__ == "__main__":
#     for test in range(int(input())):
#         n = int(input())
#         arr = [[0]*100000,[0]*100000]
#
#         for idx, var in enumerate(map(int,input().split())):
#             arr[0][idx] = var
#         for idx, var in enumerate(map(int,input().split())):
#             arr[1][idx] = var
#
#         arr[0][1] += arr[1][0]
#         arr[1][1] += arr[0][0]
#
#         for i in range(2, n):
#             arr[0][i] += max(arr[1][i-1], arr[1][i-2])
#             arr[1][i] += max(arr[0][i-1], arr[0][i-2])
#         print(max(arr[0][n-1], arr[1][n-1]))