# 동전 0
 
import sys

N, K = map(int, sys.stdin.readline().split())
moneyList = []

for i in range(N):
    m = int(sys.stdin.readline())
    moneyList.append(m)

count = 0
while True:
    if K - moneyList[i] > 0:
        K = K - moneyList[i]
        count += 1
    elif K - moneyList[i] == 0:
        K = K - moneyList[i]
        count += 1
        break
    else:
        i -= 1

print(count)
