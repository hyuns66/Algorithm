# 트리의 순회

import sys

sys.setrecursionlimit(10 ** 5)


def preorder(start, end, s, e):
    if start > end:
        return
    if s > e:
        return
    root = postorder[e]
    idx = inorder.index(root)  # 루트의 인덱스
    left_len = idx - start
    answer.append(root)  # 루트
    preorder(start, start + left_len - 1, s, s + left_len - 1)  # 왼쪽 서브트리
    preorder(start + left_len + 1, end, s + left_len, e - 1)  # 오른쪽 서브트리


n = int(sys.stdin.readline())

answer = []
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

preorder(0, n - 1, 0, n - 1)

print(*answer)
