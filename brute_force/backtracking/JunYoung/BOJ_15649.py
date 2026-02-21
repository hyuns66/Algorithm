# N과 M(1)
# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
import sys

N, M = map(int, sys.stdin.readline().split())
results = []


def backtrack(num, selected_nums):
    if num == M:
        results.append(selected_nums)
        return

    for i in range(1, N + 1):
        if i not in selected_nums:
            backtrack(num + 1, selected_nums + [i])


backtrack(0, [])
for result in results:
    print(*result)
