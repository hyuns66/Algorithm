# 완전 이진 트리

import sys

k = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
levels = [[] for _ in range(k)]


def separation(arr, depth):
    if len(arr) == 1:  # 요소가 하나밖에 없을 때
        levels[depth].extend(arr)
        return

    mid = len(arr) // 2
    levels[depth].append(arr[mid])  # 중간값=루트만 depth 레벨이므로 levels[depth]에 넣어줌
    separation(arr[:mid], depth + 1)
    separation(arr[mid + 1:], depth + 1)


separation(arr, 0)

for level in levels:
    for i in level:
        print(i, end=" ")
    print()
