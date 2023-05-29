# 듣보잡

import sys

N, M = map(int, sys.stdin.readline().split())

listen = set()
see = set()

for i in range(N):
    listen.add(sys.stdin.readline().strip())

for i in range(M):
    see.add(sys.stdin.readline().strip())

union_set = listen & see # listen.intersection(see)
list_set = list(union_set)
list_set.sort()

print(len(list_set))
for i in list_set:
    print(i)

# 그냥 listen = {} 이렇게 선언하면 딕셔너리로 선언된다.
# union을 이용해서 합집합 연산을 수행할 수 있다.
# &(intersection)을 이용하면 교집합 연산을 할 수 있다.
