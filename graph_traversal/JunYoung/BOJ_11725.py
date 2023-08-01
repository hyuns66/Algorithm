# 트리의 부모 찾기

import sys

N = int(sys.stdin.readline())

node = [set() for i in range(N)]

for i in range(N - 1):
    A, B = map(int, sys.stdin.readline().split())
    node[A - 1].add(B)
    node[B - 1].add(A)

visited = [0 for i in range(N)]
root = [0 for i in range(N)]


# print(node)

def dfs(i):
    visited[i - 1] = 1
    for n in node[i - 1]:  # 갈 수 있는 곳 중에
        if visited[n - 1] == 0:
            root[n - 1] = i  # 부모노드 입력
            dfs(n)  # 안 가본 곳이면 가보기


dfs(1)

# print(root)

for i in range(1, len(root)):
    print(root[i])

# 런타임 에러 (RecursionError)
