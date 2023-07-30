# 바이러스

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

net = [set() for i in range(N)]

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    net[A - 1].add(B)
    net[B - 1].add(A)

#print(net)

infected = [0 for i in range(N)]


def dfs(i):
    infected[i - 1] = 1
    for node in net[i - 1]: # 갈 수 있는 곳 중에
        if infected[node - 1] == 0:
            dfs(node)  # 안 가본 곳이면 가보기


dfs(1)
#print(infected)

count = 0
for i in range(len(infected)):
    if infected[i] == 1:
        count += 1

if count > 0:
    count -= 1
print(count)

# 내가 틀렸던 반례
#3
#2
#3 2
#2 1

# 양방향 간선인데, 단방향으로 취급해서 틀렸다.
