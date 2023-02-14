import sys

# 전위 순회
def preorder(node):
    global tree, answer
    answer.append(node)
    if not tree[node].is_not_left():
        preorder(tree[node].left.num)
    if not tree[node].is_not_right():
        preorder(tree[node].right.num)

# 트리 초기화
def make_tree(i_start, i_end, p_start, p_end):
    global tree, post_order, in_order
    if i_start >= i_end or p_start >= p_end:
        return
    root = post_order[p_end-1]
    for idx in range(i_start, i_end + 1):
        if in_order[idx] == root:
            if idx > p_start:
                tree[root].left = tree[post_order[p_start + idx - 1]]
            if idx < p_end-1:
                tree[root].right = tree[post_order[p_end - 1]]
            make_tree(i_start, idx - 1, p_start, p_start + idx - 1)
            make_tree(idx + 1, i_end, p_start + idx, p_end - 1)


class Node:
    def __init__(self, num):
        self.num = num
        self.right = None
        self.left = None

    def is_not_left(self):
        return self.left is None

    def is_not_right(self):
        return self.right is None


N = int(sys.stdin.readline())
tree = dict()
in_order = list(map(int, sys.stdin.readline().split()))
post_order = list(map(int, sys.stdin.readline().split()))
for p in post_order:
    tree[p] = Node(p)

start = post_order[-1]
answer = list()
make_tree(0, len(in_order), 0, len(post_order))
preorder(start)

print(*answer)
