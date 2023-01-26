import sys

c = int(sys.stdin.readline())
n = int(sys.stdin.readline())
com = [list() for i in range(c + 1)]
visited = [False] * (c + 1)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    com[a].append(b)
    com[b].append(a)

stack = list()
stack.append(1)
visited[1] = True
answer = 0
while stack:
    cur = stack.pop()
    for node in com[cur]:
        if not visited[node]:
            answer += 1
            stack.append(node)
            visited[node] = True

print(answer)