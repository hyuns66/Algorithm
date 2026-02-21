# N과 M (2)
# 길이가 M인 오름차순 수열
import sys

N, M = map(int, sys.stdin.readline().split())

answers = []


def backtracking(start, selected_num, M):
    # 길이를 만족하면 종료
    if len(selected_num) == M:
        # print(selected_num)
        answers.append(selected_num)

    for i in range(start, N + 1):
        backtracking(i + 1, selected_num + [i], M)


backtracking(1, [], M)

for i in answers:
    print(*i)
