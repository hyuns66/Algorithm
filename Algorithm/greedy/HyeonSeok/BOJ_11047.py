import sys

N, K = map(int, sys.stdin.readline().split())
cursor = N-1
answer = 0
coins = list()
for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

while K > 0:
    while K >= coins[cursor]:
        K -= coins[cursor]
        answer += 1
    cursor -= 1

print(answer)