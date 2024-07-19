# N과 M(10)

import sys

# N개의 자연수 중에서 M개를 고른 수열
# 고른 수열은 비내림차순이어야 한다.
# 중복되는 수열을 여러 번 출력하면 안되며 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

answers = set()


def backtracking(selected_num, last, visited_index):
    if len(selected_num) == M:
        answers.add(tuple(selected_num))
        return
    for i in range(N):
        if N_list[i] >= last and i not in visited_index:
            backtracking(selected_num + [N_list[i]], N_list[i], visited_index | {i})


backtracking([], 0, set())

answers = list(answers)
answers.sort()

for a in answers:
    print(*a)
