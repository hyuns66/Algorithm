import sys

# def down_tree(node, cost):
#     global visited, leaf_cost
#     visited[node] = True
#     node_num = len(data_set[node]) - 1
#     if node_num == 0 and node != 1:
#         leaf_cost.append(cost)
#         return
#     for n in data_set[node]:
#         if not visited[n]:
#             down_tree(n, cost/node_num)


N, W = map(int, sys.stdin.readline().split())

data_set = [list() for i in range(N+1)]
visited = [False] * (N+1)
# nodes = [list() for j in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    data_set[a].append(b)
    data_set[b].append(a)

answer = 0
for i in range(2, N+1):
    if len(data_set[i]) == 1:
        answer += 1
# visited[0] = True
# data_set[1].append(0)
# leaf_cost = list()
# stack = [(1, W)]
# while stack:
#     cur_node, cost = stack.pop()
#     visited[cur_node] = True
#     node_num = len(data_set[cur_node]) - 1
#     if node_num == 0 and cur_node != 1:
#         leaf_cost.append(cost)
#         continue
#     for node in data_set[cur_node]:
#         if not visited[node]:
#             stack.append((node, cost/node_num))

# answer = 0
# for l in leaf_cost:
#     answer += l

print(W / answer)