# 이진 검색 트리
import sys

sys.setrecursionlimit(10 ** 3)


def postorder(start, end):
    if start > end:
        return
    root = numbers[start]
    pivot = end + 1
    for i in range(start + 1, end + 1):  # start+1부터 end까지
        if int(root) < int(numbers[i]):  # 루트보다 큰 값이 나오면 그 값부터 오른쪽 서브트리다.
            pivot = i  # 해당값을 pivot으로 표현
            break

    postorder(start + 1, pivot - 1)
    postorder(pivot, end)
    print(root)


numbers = []
f = open("BOJ_5639_input.txt", 'r')
lines = f.readlines()
for line in lines:
    numbers.append(line.strip())

postorder(0, len(numbers) - 1)

"""
틀린 방법 1

# 이진 검색 트리

import sys

def split(list):
    root = list[0]
    left = []
    right = []
    for i in range(1, len(list)):
        if int(list[i]) < int(root):  # 루트보다 작은값은 왼쪽에
            left.append(list[i])
        else:  # 루트보다 큰값은 오른쪽에
            right.append(list[i])

    tree[root] = ['.' if len(left) == 0 else left[0], '.' if len(right) == 0 else right[0]]
    # left, right 의 첫번째 요소가 왼쪽 자식노드, 오른쪽 자식 노드가 된다. 없으면 '.'로 부여함

    if len(left) != 0:
        split(left)
    if len(right) != 0:
        split(right)


def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node)


numbers = []
lines = sys.stdin.readlines()
for line in lines:
    numbers.append(line.strip())

tree = dict()
split(numbers)

postorder(numbers[0])
"""
