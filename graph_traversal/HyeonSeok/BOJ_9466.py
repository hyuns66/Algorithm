import sys
sys.setrecursionlimit(10 ** 5)

def DFS(idx, visited, node):
    global cnt, finish
    if not visited[node]:
        visited[node] = True
        DFS(idx, visited, test_case[idx][1][node-1])
    else:
        if not finish[node - 1]:
            temp = test_case[idx][1][node - 1]
            cnt += 1
            while temp != node:
                cnt += 1
                temp = test_case[idx][1][temp - 1]
    finish[node - 1] = True


T = int(sys.stdin.readline().rstrip())
test_case = list()
cnt = 0
finish = list()

for _ in range(T):
    num = int(sys.stdin.readline())
    test_case.append((num, list(map(int, sys.stdin.readline().split()))))

for i in range(T):
    visited = [False] * (test_case[i][0] + 1)
    finish = [False] * test_case[i][0]
    visited[0] = True
    cnt = 0
    for j in range(test_case[i][0]):
        DFS(i, visited, j + 1)
    print(test_case[i][0] - cnt)