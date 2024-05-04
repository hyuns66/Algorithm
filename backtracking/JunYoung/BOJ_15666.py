# N과 M(12)
# N개의 자연수 중에서 M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다
# 중복되는 수열을 여러 번 출력하면 안되며

import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()


def backtracking(start, selected_num):
    answer = set()
    if len(selected_num) == M:
        answer.add(tuple(selected_num))
        return answer

    for i in range(start, N):
        answer |= backtracking(i, selected_num + [N_list[i]]) # 기호말고 코드로 쓰려면 update

    return answer

answer = backtracking(0, [])

for comb in sorted(answer):
    print(*comb)  # 각 조합을 공백을 이용하여 출력