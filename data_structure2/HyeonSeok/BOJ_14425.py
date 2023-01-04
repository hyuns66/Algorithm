import sys

N, M = map(int, sys.stdin.readline().split())
S = set()
cnt = 0

for i in range(N):
    word = sys.stdin.readline().rstrip()
    S.add(word)

for j in range(M):
    word = sys.stdin.readline().rstrip()
    if word in S:
        cnt += 1

print(cnt)