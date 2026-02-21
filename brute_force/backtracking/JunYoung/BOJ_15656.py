# N과 M (7)

# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.

import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

N_list.sort()

answers = []
def back_tracking(selected_num):
    if len(selected_num) == M:
        answers.append(selected_num)
        return

    for i in range(N):
        back_tracking(selected_num+[N_list[i]])

back_tracking([])

for i in answers:
    print(*i)
