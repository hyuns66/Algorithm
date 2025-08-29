import sys
sys.setrecursionlimit(10**5)

def get_root(postorder, start_idx, length):
    return postorder[start_idx + length - 1]

def add_child(idx, cur_node, inorder, postorder, visited, answer, li, ri):
    if visited[idx]:
        return
    visited[idx] = True
    answer.append(cur_node)
    if idx > 0:
        left_node_data = get_root(postorder, li, idx - li)
        add_child(idx-1, left_node_data, inorder, postorder, visited, answer, li, idx-1)
    if idx < len(inorder) - 1:
        right_node_data = get_root(postorder, idx+1, ri - idx - 1)
        add_child(idx+1, right_node_data, inorder, postorder, visited, answer, idx+1, ri)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
root_data = get_root(postorder, 0, len(postorder))
cur_idx = -1
for i in range(N):
    if inorder[i] == root_data:
        cur_idx = i
        break
visited = [False for _ in range(N)]
answer = list()
add_child(cur_idx, root_data, inorder, postorder, visited, answer, 0, N-1)
print(*answer)