# 나무 위의 빗물

import sys


def stack_dfs(start):
    stack = [start]
    leaf_node = 0

    while stack:
        current_node = stack.pop()
        visited[current_node] = 1
        flag = True

        for child in tree[current_node]:
            if visited[child] == 0:
                stack.append(child)
                flag = False

        if flag:
            leaf_node += 1

    return leaf_node


N, W = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)

visited = [0 for _ in range(N + 1)]
leaf_node = stack_dfs(1)

print(W / leaf_node)

"""
(오답)

import sys
sys.setrecursionlimit(10 ** 4)

def dfs(i):
    visited[i] = 1
    global leaf_node
    flag = True
    for child in tree[i]:
        if visited[child] == 0:
            flag = False
            dfs(child)
    if flag:
        leaf_node += 1


N, W = map(int, sys.stdin.readline().split())

tree = [[] for _ in range(N + 1)]
for i in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)

leaf_node = 0
visited = [0 for _ in range(N + 1)]
dfs(1)

print(W/leaf_node)

"""
