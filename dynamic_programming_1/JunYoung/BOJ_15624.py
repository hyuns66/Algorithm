# 피보나치 수 7

import sys

n = int(sys.stdin.readline())
memo = [0 for _ in range(max(2,n+1))] #n+2까지로 해야 n+1만큼 만들어줌 -> 아닌데..?

memo[0] = 0
memo[1] = 1 # 최소 여기까지는 배열이 생성되게 해서 index 에러 안나게 하기!

for i in range(2, n+1):
    memo[i] = (memo[i-2] + memo[i-1]) % 1000000007

print(memo[n])
## dp값 저장할때 나머지 연산을 한 결과를 저장! 안그러면 너무 큰수가 많이 저장돼 메모리 초과 난다.