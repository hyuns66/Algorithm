# RGB거리
import sys

N = int(sys.stdin.readline())
costs = []
for i in range(N):
    costs.append(list(map(int, sys.stdin.readline().split())))

for house_index in range(1, N):
    for i in range(3):  # 빨,초,파
        min_cost = sys.maxsize
        for j in range(3):
            if i == j:
                continue  # 같은 색 못칠함
            else:
                possible_cost = costs[house_index - 1][j] + costs[house_index][i]
                min_cost = min(min_cost, possible_cost)
        costs[house_index][i] = min_cost

print(min(costs[N - 1]))
