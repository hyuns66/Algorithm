"""
전체 리스트에서 K-1개만 딱 고르면 비용은 자동산출됨
-> 각 고른 원소는 각 조의 맨 마지막 사람을 의미하므로
"""

"""
시간초과 코드
-> 모든 경우의 수를 탐색했기 때문
그리디로 해야되는뎅 어케함?
"""
# import itertools
# import sys
#
# N, K = map(int, sys.stdin.readline().split())
# children = list(map(int, sys.stdin.readline().split()))
# positions = [i for i in range(N)]
# answer = sys.maxsize
# marker = itertools.combinations(positions, K-1)
#
# if K == 1:
#     print(children[-1] - children[0])
#     sys.exit(0)
#
# for m in marker:
#     temp = 0
#     if m[-1] == N-1:
#         continue
#     if m[0] != 0:
#         temp += children[m[0]] - children[0]
#     for i in range(1, K-1):
#         if (m[i] - m[i-1]) > 1:
#             temp += children[m[i]] - children[m[i-1] + 1]
#     temp += children[-1] - children[m[-1] + 1]
#     answer = min(answer, temp)
#
# print(answer)

"""
그리디 코드
-> K = N 으로 가정해서 1인 1팀을 기준으로 시작
N-K만큼 반복하며 가장 차이가 작은 둘씩 짝지음
"""
import sys

N, K = map(int, sys.stdin.readline().split())
children = list(map(int, sys.stdin.readline().split()))
visited = [False] * (N-1)
height_diff = list()
answer = 0

for i in range(N-1):
    height_diff.append(children[i+1] - children[i])

# 키차이를 이용해서 정렬 후 그리디알고리즘 적용
height_diff.sort()
for i in range(N-K):
    answer += height_diff[i]

print(answer)