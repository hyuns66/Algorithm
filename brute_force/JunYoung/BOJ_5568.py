# 카드 놓기

import sys
import itertools

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = []

for i in range(n):
    cards.append(int(sys.stdin.readline()))

comb = list(itertools.combinations(cards, k))

numbers = set()

for i in comb:
    perms = itertools.permutations(i, k)
    for perm in perms:
        number = int(''.join(str(d) for d in perm))
        numbers.add(number)

print(len(numbers))

# join() 메소드는 문자열을 이어붙이는 역할을 한다. join 앞에 있는건 구분자
