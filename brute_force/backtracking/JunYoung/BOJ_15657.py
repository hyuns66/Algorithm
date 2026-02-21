# N과 M(8)
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다.


import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

answers = []


def backtracking(start, selected_num):
    if len(selected_num) == M:
        answers.append(selected_num)
        return

    for i in range(start, N):
        backtracking(i, selected_num + [N_list[i]]) # [주의] 여기에 start가 아니라 i를 넣어야해!!!!


backtracking(0, [])
for a in answers:
    print(*a)
