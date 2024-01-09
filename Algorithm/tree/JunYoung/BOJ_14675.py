# 단절점과 단절선

import sys

N = int(sys.stdin.readline())
tree = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a - 1].append(b)
    tree[b - 1].append(a)

q = int(sys.stdin.readline())
for i in range(q):
    t, k = map(int, sys.stdin.readline().split())
    if t == 1:  # 노드k가 단절점인지?
        if len(tree[k - 1]) >= 2:
            print("yes")
        else:
            print("no")
    else:  # k번째의 입력의 간선이 단절선인지?
        print("yes")
