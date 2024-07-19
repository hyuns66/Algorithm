# 평범한 배낭
# 최대 K 무게까지만 배낭에 넣을 수 있다고 했을 때, 얻을 수 있는 최대의 가치?

# import sys
#
# N, K = map(int, sys.stdin.readline().split())
#
# dp = [0 for _ in range(K + 1)]  # 무게에 따른 최대가치
#
# items = []
# for i in range(N):
#     W, V = map(int, sys.stdin.readline().split())
#     items.append((W, V))
#     dp[W] = max(V, dp[W])  # 입력받은 아이템으로 dp 값 초기화
#
# for w in range(1, K + 1):  # 백팩 무게 w부터 K까지 갱신
#     for item in items:
#         item_w = item[0]  # 아이템 무게
#         if w - item_w < 1:  # 백팩 무게 - 아이템 무게가 1보다 작으면 못담음
#             continue
#         else:  # 해당 아이템을 담을 수 있다면
#             dp[w] = max(dp[w], dp[w - item_w] + item[1])
#
# print(dp)
# print(dp[K])

# 점화식
# dp[w] = min(dp[w-item1.w]+item1.value, dp[w-item2.w]+item2.value, ...)

# 아..! 물건은 각 하나씩이구나..?!
# 그럼 item이 무한인거 마냥 풀 순 없겠군

import sys

n, k = map(int, sys.stdin.readline().split())
items = [[0,0]]
for i in range(n):
     w, v = map(int, sys.stdin.readline().split())
     items.append((w, v))

dp = [[0]*(k+1) for _ in range(n+1)] # n행 k열 (n: 물건개수, k: 배낭 무게)
for i in range(1, n+1):
    for j in range(1, k+1):
        weight = items[i][0]
        value = items[i][1]
        if j < weight: # 가방에 넣을 수 없으면
            dp[i][j] = dp[i-1][j] # 위에 값 그대로 가져오기
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[n][k])

# 답지 보고 품