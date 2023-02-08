import sys
n, m = map(int, sys.stdin.readline().split())
answer = 1
for _ in range(m):
    answer *= n
    n -= 1
print("asdf : ", answer)
for i in range(2, m+1):
    answer //= i    # 몫 연산
    print(answer)
print(answer)
