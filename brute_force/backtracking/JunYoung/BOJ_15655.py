# N과 M (6)

# N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

answers = []


def backtracking(start, selected_num):
    #print(selected_num)
    if len(selected_num) == M:
        answers.append(selected_num)
        return

    for i in range(start, N):
        backtracking(i + 1, selected_num + [N_list[i]])


backtracking(0, [])

for a in answers:
    print(*a)
