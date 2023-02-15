import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
mem = [1] * N
answer = 1
for i in range(1, N):
    cnt = 1
    flag = False
    for j in range(i):
        if sequence[j] < sequence[i]:
            cnt = max(cnt, mem[j])
            flag = True
    if flag:
        cnt += 1
    mem[i] = cnt
    answer = max(answer, cnt)

print(answer)