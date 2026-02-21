# N과 M(9)

import sys

# 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))

answers = set()


def backtracking(selected_num, visited):
    if len(selected_num) == M:
        answers.add(tuple(selected_num))
        return
    for i in range(0, N):
        if i not in visited:
            backtracking(selected_num + [N_list[i]], visited | {i})


backtracking([], set())

answers = sorted(answers)

for a in answers:
    print(*a)

# 시간 초과
# 중복 제거에는 set() 만한게 없구만!