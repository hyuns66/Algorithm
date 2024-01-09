import sys
from collections import deque


def two_k_shuffle(k, c):
    d = deque(c)
    cards = c
    for i in range(1, k+2):
        d.rotate(1 << (k + 1 - i))
        cards[0: len(d)] = list(d)
        d = deque(cards[0: 1 << (k - i + 1)])
    return cards


N = int(sys.stdin.readline())
result = list(map(int, sys.stdin.readline().split()))
temp = N
K = 1
while temp != 1:
    temp = temp >> 1
    K += 1

ca = [i+1 for i in range(N)]
for i in range(K):
    for j in range(K):
        cards = [k+1 for k in range(N)]
        after_shuffle = two_k_shuffle(j, two_k_shuffle(i, cards))
        if after_shuffle == result:
            print(i, j)
            exit()
