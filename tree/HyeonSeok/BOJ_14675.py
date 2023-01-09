import sys

N = int(sys.stdin.readline())
tree = [list() for i in range(N+1)]
answer = list()

for i in range(N-1):
    node_a, node_b = map(int, sys.stdin.readline().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

q = int(sys.stdin.readline())

for i in range(q):
    op, par = map(int, sys.stdin.readline().split())
    if op == 2:
        answer.append("yes")
    elif op == 1:
        if len(tree[par]) > 1:
            answer.append("yes")
        else:
            answer.append("no")

for a in answer:
    print(a)