# 1,2,3 더하기
# top-down 형식으로 풀어봄

import sys

# n은 양수이며 11보다 작다. 1<=n<11
memo = [0 for _ in range(11)]  # index: 0~10
memo[1] = 1 # 1
memo[2] = 2 # 1+1, 2
memo[3] = 4 # 1+2, 1+1+1, 2+1, 3

def cal(n):
    if n <= 0:
        return 0
    if memo[n] != 0:
        return memo[n]
    else:
        memo[n] = cal(n - 1) + cal(n - 2) + cal(n - 3)
        return memo[n]

answer = []
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    result = cal(n)
    answer.append(result)

for a in answer:
    print(a)
