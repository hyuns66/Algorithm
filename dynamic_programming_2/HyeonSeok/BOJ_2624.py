import sys
input = sys.stdin.readline

T = int(input())
k = int(input())
cash_register = []
dp = [0] * (T+1) #n 금액에 대한 동전 교환 방법 가지 수
dp[0] = 1 
for _ in range(k):
    p , n = map(int, input().split())
    cash_register.append((p, n))

for coin, count in cash_register:
    for money in range(T, 0, -1): #T원부터 1원까지 내려가면서 반복문
        for i in range(1, count + 1): #현재 coin의 개수만큼 반복문
            if money - coin * i >= 0:
                dp[money] += dp[money - coin * i]

print(dp[T])