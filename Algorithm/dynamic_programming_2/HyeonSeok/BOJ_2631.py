import sys

# binary_search  O(nlogn)
# def binary_search(array, start, end, tar):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] < tar:
#             start = mid + 1
#         elif array[mid] > tar:
#             end = mid
#             if start == end:
#                 break
#         else:
#             break
#     return mid
#
# N = int(sys.stdin.readline())
# children = list()
# lis = [0] * N
# length = 0
# for i in range(N):
#     children.append(int(sys.stdin.readline()))
# for i, child in enumerate(children):
#     if length == 0:
#         lis[0] = child
#         length += 1
#     else:
#         idx = binary_search(lis, 0, length, child)
#         lis[idx] = child
#         if idx == length:
#             length += 1
#
# print(lis)
# print(length)
# 3 7 5 2 6 1 4
# 3
# 3 7
# 3 5
# 2 5
# 2 5 6
# 1 5 6
# 1 4 6

# dp    O(N^2)
N = int(sys.stdin.readline())
children = list()
dp = [1] * N
prev_ids = [-1] * N
for i in range(N):
    children.append(int(sys.stdin.readline()))
for i, child in enumerate(children):
    point = i - 1
    while point >= 0:
        if children[point] < child and dp[i] < dp[point] + 1:
            dp[i] = dp[point] + 1
            prev_ids[i] = point
        point -= 1

print(children)
print(prev_ids)
print(dp)

cur_idx = max(range(len(dp)), key=lambda i: dp[i])
real_lis = list()
while True:
    real_lis.append(children[cur_idx])
    cur_idx = prev_ids[cur_idx]
    if cur_idx < 0:
        break
print(real_lis)
print(N - max(dp))