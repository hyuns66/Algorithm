# 모든 순열
import sys
import itertools

N = int(sys.stdin.readline())

permutations = list(itertools.permutations([i for i in range(1,N+1)], N))
for i in permutations:
    print(*i)
