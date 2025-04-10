import sys

def calc_district_diff(graph, dy, dx, d1, d2):
    global total_sum
    five_sum = total_sum

    print(dy, dx, d1, d2)
    min_sum = sys.maxsize
    max_sum = 0
    # 1 구역
    sum = 0
    for y in range(0, dy+d1):
        for x in range(0, dx+1-y):
            sum += graph[y][x]
            print(y, x)
    min_sum = min(min_sum, sum)
    max_sum = max(max_sum, sum)
    five_sum -= sum
    # 2 구역
    sum = 0
    for y in range(0, dy+d2+1):
        for x in range(dx+1, N):
            sum += graph[y][x]
    min_sum = min(min_sum, sum)
    max_sum = max(max_sum, sum)
    five_sum -= sum
    # 3 구역
    sum = 0
    for y in range(dy+d1, N):
        for x in range(0, dx-d1+d2):
            sum += graph[y][x]
    min_sum = min(min_sum, sum)
    max_sum = max(max_sum, sum)
    five_sum -= sum
    # 4 구역
    sum = 0
    for y in range(dy+d2+1, N):
        for x in range(dx-d1+d2, N):
            sum += graph[y][x]
    min_sum = min(min_sum, sum)
    max_sum = max(max_sum, sum)
    five_sum -= sum
    # 5 구역
    min_sum = min(min_sum, five_sum)
    max_sum = max(max_sum, five_sum)

    return max_sum - min_sum

N = int(input())
graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))
total_sum = sum(sum(g) for g in graph)
answer = sys.maxsize

# for y in range(N):
#     for x in range(N):
#         for d1 in range(1, N):
#             for d2 in range(1, N):
#                 if d1 >= 1 and d2 >= 1 and 0 <= y < y+d1+d2 <= N-1 and 0 <= x-d1 < x < x+d2 <= N-1:
#                     answer = min(answer , calc_district_diff(graph, y, x, d1, d2))
# print(answer)

calc_district_diff(graph, 2, 2, 1, 1)