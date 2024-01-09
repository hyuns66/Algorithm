import sys


class Node:
    def __init__(self, char):
        self.right = None
        self.left = None
        self.char = char

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def inorder(node):
    global nodes
    if nodes[node].left is not None:
        inorder(nodes[node].left.char)
    print(node, end="")
    if nodes[node].right is not None:
        inorder(nodes[node].right.char)


def preorder(node):
    global nodes
    if nodes[node].left is not None:
        preorder(nodes[node].left.char)
    if nodes[node].right is not None:
        preorder(nodes[node].right.char)
    print(node, end="")

N = int(sys.stdin.readline())
nodes = dict()
for _ in range(N):
    char, left, right = sys.stdin.readline().split()
    for n in [char, left, right]:
        if n not in nodes and n != '.':
            nodes[n] = Node(n)
    if left != '.':
        nodes[char].set_left(nodes[left])
    if right != '.':
        nodes[char].set_right(nodes[right])

stack = list()
stack.append('A')
while stack:
    current = stack.pop()
    print(current, end="")
    if nodes[current].left is None and nodes[current].right is None:
        continue
    if nodes[current].right is not None:
        stack.append(nodes[current].right.char)
    if nodes[current].left is not None:
        stack.append(nodes[current].left.char)
print("")

inorder('A')
print("")
preorder('A')
