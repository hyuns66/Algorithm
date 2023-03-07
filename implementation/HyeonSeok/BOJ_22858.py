import sys

N, K = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))
D = list(map(int, sys.stdin.readline().split()))


for _ in range(K):
    temp = [0] * N
    for i in range(N):
        temp[D[i]-1] = S[i]
    S = temp[:]

print(*S)