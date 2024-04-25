# N과 M (3)
# 같은 수를 여러 번 골라도 된다. 길이가 M인 수열
import sys

N, M = map(int, sys.stdin.readline().split())

answers = []


def backtracking(start, selected_num, M):
    if len(selected_num) == M: # 유망함수
        answers.append(selected_num)
        return

    for i in range(start, N + 1):
        backtracking(start, selected_num + [i], M)


backtracking(1, [], M)


for i in answers:
    print(*i)
