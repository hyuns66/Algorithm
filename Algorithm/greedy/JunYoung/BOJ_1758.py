# 알바생 강호

import sys

N = int(sys.stdin.readline())
customers = []
for i in range(N):
    customers.append(int(sys.stdin.readline()))
customers.sort(reverse=True)

tip = 0
count = 0
for i in range(N):
    #print(customers[i] - count)
    if customers[i] - count > 0:
        tip += customers[i] - count
        count += 1
    else:
        break

print(tip)

