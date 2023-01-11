import sys

N, M = map(int, sys.stdin.readline().split())
items = [i for i in range(1, N+1)]
err = [list() for i in range(N+1)]
answer = 0

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    err[min(a, b)].append(max(a,b))

for i in range(1, N+1):
    err_set_1 = err[i]
    for j in range(i+1, N+1):
        if j in err_set_1:
            continue
        err_set_2 = err_set_1 + err[j]
        for k in range(j+1, N+1):
            if k in err_set_2:
                continue
            answer += 1

print(answer)
