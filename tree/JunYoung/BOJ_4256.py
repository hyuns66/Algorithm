# 트리

import sys


def postorder(start, end, s, e):
    if start > end:
        return
    if s > e:
        return

    root = preorder[start]

    left_len = 0
    for i in range(s, e + 1):  # start+1부터 end까지
        if int(root) == inorder[i]:  # 중위 순회 결과에서 루트가 나오면 그 전까지가 왼쪽 서브트리다.
            break
        left_len += 1

    postorder(start + 1, start+left_len, s, s+left_len-1)
    postorder(start+left_len+1, end, s+left_len+1, e)
    answer.append(root)


T = int(sys.stdin.readline())
answers = []
for _ in range(T):
    n = int(sys.stdin.readline())
    answer = []
    preorder = list(map(int, sys.stdin.readline().split()))
    inorder = list(map(int, sys.stdin.readline().split()))

    postorder(0, n-1, 0, n-1)
    answers.append(answer)

for i in answers:
    print(*i)
