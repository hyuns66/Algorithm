T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    temp = 1
    for i in range(N):
        temp *= (M-i)
    for i in range(N):
        temp //= (i+1)
    print(temp)