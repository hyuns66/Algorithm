# 트리의 순회

import sys

sys.setrecursionlimit(10 ** 5)


def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end:
        return
    if post_start > post_end:
        return
    root = postorder[post_end]
    idx = inorder.index(root)  # 루트의 인덱스
    left_len = idx - in_start
    answer.append(root)  # 루트
    preorder(in_start, in_start + left_len - 1, post_start, post_start + left_len - 1)  # 왼쪽 서브트리
    preorder(in_start + left_len + 1, in_end, post_start + left_len, post_end - 1)  # 오른쪽 서브트리


n = int(sys.stdin.readline())

answer = []
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

preorder(0, n - 1, 0, n - 1)

print(*answer)
