# 소수의 연속합

import sys


# 에라토스테네스의 체
def find_prime_list(n):
    sieve = [True] * (n+1)

    m = int(n ** 0.5)
    for i in range(2, m + 1):  # 2~루트n까지
        if sieve[i] == True:
            for j in range(2 * i, len(sieve), i):
                sieve[j] = False
    #print(sieve)
    # 2~n까지의 소수 리스트 반환
    return [i for i in range(2, n+1) if sieve[i] == True]


N = int(sys.stdin.readline())
prime_list = find_prime_list(N)

#print(prime_list)
# 누적합 계산
for i in range(1, len(prime_list)): # 인덱스1 부터 누적합 계산
    prime_list[i] += prime_list[i - 1]

start_idx = 0
end_idx = 0
answer = 0
#print(prime_list)

while end_idx < len(prime_list):
    #print(f"why? {0 if start_idx-1<0 else prime_list[start_idx-1]}")
    prime_sum = prime_list[end_idx] - (0 if start_idx-1<0 else prime_list[start_idx-1])
    if prime_sum < N:
        end_idx += 1
    else:
        #print(f"{prime_sum} = {start_idx}")
        #print(prime_sum)
        if prime_sum == N:
            #print(f"{prime_list[start_idx]}~{prime_list[end_idx]}")
            answer += 1
        start_idx += 1

print(answer)
