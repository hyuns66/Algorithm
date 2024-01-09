# 퇴사

import sys
import itertools


def generate_combinations(n):
    options = [0, 1]
    combinations = list(itertools.product(options, repeat=n))
    return combinations


N = int(sys.stdin.readline())

T = []
P = []

for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

all_combinations = generate_combinations(N)
possible_combinations = []

for comb in all_combinations:
    days = [0 for i in range(N)]
    flag = True
    for j in range(len(comb)):
        if comb[j] == 1:
            if (j + T[j])>N:
                flag = False
                break
            for t in range(j, j + T[j]):
                if days[t] == 1:
                    flag = False
                    break
                days[t] = 1
            if not flag:
                break
    if flag:
        possible_combinations.append(comb)

#print(possible_combinations)

possible_price = []
for c in possible_combinations:
    price = 0
    for i in range(N):
        if c[i] == 1:
            price += P[i]
    possible_price.append(price)

possible_price.sort(reverse=True)
print(possible_price[0])
