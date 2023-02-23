import sys

# 출력함수
def print_node(tree_list: list, length, r):
    if length == 1:
        rank_list[r].append(tree_list[0])
        return
    else:
        rank_list[r].append(tree_list[int(length / 2)])
    left_tree = tree_list[0:int(length / 2)]
    right_tree = tree_list[int(length / 2 + 1):length]
    r += 1
    print_node(left_tree, len(left_tree), r)
    print_node(right_tree, len(right_tree), r)


K = int(sys.stdin.readline())
rank_list = [list() for i in range(K)]
tree_map = list(map(int, sys.stdin.readline().split()))
print_node(tree_map, len(tree_map), 0)

for rank in rank_list:
    print(*rank)
