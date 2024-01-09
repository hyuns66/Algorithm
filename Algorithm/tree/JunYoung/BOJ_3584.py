import sys
sys.setrecursionlimit(10 ** 4)

T = int(sys.stdin.readline())


def dfs(a):
    root.append(a)
    if len(tree[a]) == 0:
        return
    parent = tree[a][0]
    dfs(parent)


for i in range(T):
    N = int(sys.stdin.readline())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())  # 부모, 자식
        tree[B].append(A)

    # a, b의 공통 조상을 구하기
    a, b = map(int, sys.stdin.readline().split())
    root = []
    dfs(a)
    root_a = root.copy()
    root.clear()
    dfs(b)

    common_elements = [element for element in root if element in root_a]
    print(common_elements[0])
