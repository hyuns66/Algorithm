import sys

sys.setrecursionlimit(100000)

# 후위 순이므로 좌 -> 우 -> 부모 순서로 출력 (cur_node가 부모)
def post_order(cur_node):
    global node
    if cur_node == 0:
        return
    post_order(node[cur_node][1])   # Left 탐색
    post_order(node[cur_node][2])   # Right 탐색
    print(cur_node)
    
# n 노드의 위치 찾아서 node에 정보 삽입 후 return
def find_position(cur_node, n):
    global node
    if cur_node > n:
        if node[cur_node][1] == 0:
            node[cur_node][1] = n
            node[n][0] = cur_node
            return
        else:
            find_position(node[cur_node][1], n)
    else:
        if node[cur_node][2] == 0:
            node[cur_node][2] = n
            node[n][0] = cur_node
            return
        else:
            find_position(node[cur_node][2], n)
    
node = dict()   # [parent, left, right]
root_node = int(sys.stdin.readline())
node[root_node] = [0, 0, 0]

# 전위순회 기록 바탕으로 트리 구성
for line in sys.stdin:
    try:
        u = int(line)
        node[u] = [0,0,0]
        find_position(root_node, u)
    except:
        break

# 후위순회 돌면서 출력
post_order(root_node)
