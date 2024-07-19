# N과 M(11)
# 같은 수를 여러 번 골라도 된다.
# 중복되는 수열을 여러 번 출력하면 안된다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

N_list = list(set(N_list))
N_list.sort()

answers = []


def backtracking(selected_num):
    if len(selected_num) == M:
        answers.append(selected_num)
        return
    for i in range(len(N_list)):
        backtracking(selected_num + [N_list[i]])


backtracking([])

for a in answers:
    print(*a)
