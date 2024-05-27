# 수들의 합 4
# 부분 합 중 합이 K인 것이 몇개나 있는지 구하시오.
import sys

N, K = map(int, sys.stdin.readline().split())
vals = list(map(int, sys.stdin.readline().split()))

# 부분 합 구하기
dict = {0 :1}
sum = 0
count = 0
for i in range(N):
    sum += vals[i]
    if sum-K in dict:
        count += dict[sum-K]
    if sum in dict:
        dict[sum] += 1
    else:
        dict[sum] = 1

print(count)
