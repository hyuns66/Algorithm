import sys

N = int(sys.stdin.readline())
graph = list(map(int, sys.stdin.readline().split()))
fb = 0
ff_graph =[0] * N
for i in range(1, N-1):
    ff_graph[i] = ff_graph[i-1] + graph[i]
fb = ff_graph[N-1]
print(ff_graph)