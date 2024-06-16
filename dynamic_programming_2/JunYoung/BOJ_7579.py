# 앱
# 비활성화 했을 경우의 비용 ci의 합을 최소화하여 필요한 메모리 M 바이트를 확보하는 방법
import sys

n, m = map(int, sys.stdin.readline().split())
memory = [0]+list(map(int, sys.stdin.readline().split()))
cost = [0]+list(map(int, sys.stdin.readline().split()))

# 필요한 메모리 m 바이트를 확보하기 위한 최소비용을 계산

#============
#냅색 문제랑 비슷한 것 같으면서... 모르겠군.
#=> 냅색이랑 정확히 같다!

knapsack = [[0] * (sum(cost)+1) for _ in range(n+1)]
answer = sum(cost)

for i in range(1, n+1):
    for j in range(0, sum(cost)+1):
        if j < cost[i]:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-cost[i]]+memory[i])

        if knapsack[i][j] >= m:
            answer = min(answer, j)

#print(knapsack)
print(answer)

#[이 케이스 고려 안했었음]
#5 60
#30 10 20 35 40
#0 1 0 0 0