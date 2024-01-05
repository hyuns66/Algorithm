# 트리의 지름

import sys

sys.setrecursionlimit(10 ** 4)

n = int(sys.stdin.readline())
tree = [[] for _ in range(n + 1)]

for i in range(n - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    tree[parent].append([child, weight])
    tree[child].append([parent, weight])


def dfs(start, distance):
    for node, weight in tree[start]:
        if visited[node] == -1:
            visited[node] = distance + weight
            dfs(node, visited[node])


visited = [-1] * (n + 1)

# 임의 노드(i)
i = 1  # 1~n까지 아무 노드나 해도 가능! 일단 루트노드가 1로 주어졌으니 루트노드로 해주었다.
visited[i] = 0
dfs(i, 0)
# visited 리스트에서 가장 큰 값을 가진 요소의 인덱스를 찾습니다.
far_node = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[far_node] = 0
dfs(far_node, 0)

print(max(visited))
