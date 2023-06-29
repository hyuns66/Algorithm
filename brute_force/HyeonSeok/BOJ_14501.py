import sys


def calc_pay(day, pay):
    global N, ans
    if day >= N and ans < pay:
        ans = pay
        return
    for i in range(day, N):
        t_ = T[i]
        p_ = P[i]
        if i + t_ - 1 < N:
            new_pay = pay + p_
            calc_pay(i + t_, new_pay)
        else:
            if ans < pay:
                ans = pay
                return


N = int(sys.stdin.readline())

T = []
P = []
for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)

ans = 0
calc_pay(0, 0)
print(ans)
