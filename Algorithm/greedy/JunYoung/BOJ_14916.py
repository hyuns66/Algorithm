# 거스름돈

import sys

n = int(sys.stdin.readline())

coins = 0

while True:

    if n == 0:
        print(coins)
        break
    elif n < 2:
        print(-1)
        break
    elif n % 5 == 0:
        n -= 5
        coins += 1
    else:
        n -= 2
        coins += 1

