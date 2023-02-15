import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
mem = [1] * N

for i in range(1, N):
    cnt = 1
    for j in range(i):
        cnt = max(cnt, mem[j])
