def dfs(graph, start):
    stack = list()
    visited = [False for _ in range(N)]
    visited[start] = True
    stack.append(start)
    count = 0
    while stack:
        node = stack.pop()
        count += 1
        for tar in graph[node]:
            if visited[tar]:
                continue
            visited[tar] = True
            stack.append(tar)
    return count

N, M = map(int, input().split())
small = [[] for _ in range(N)]
big = [[] for _ in range(N)]
for m in range(M):
    a, b = map(int, input().split())
    big[a-1].append(b-1)
    small[b-1].append(a-1)

answer = 0
for i in range(N):
    count = dfs(small, i) + dfs(big, i)
    if count == N+1:
        answer += 1
print(answer)