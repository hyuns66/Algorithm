import sys
from collections import deque

t = int(sys.stdin.readline())
test_case = [list() for j in range(t)]

for i in range(t):
    n = int(sys.stdin.readline())
    for j in range(n+2):
        a, b = map(int, sys.stdin.readline().split())
        if j == 0:
            test_case[i].append(("point", j, a, b))
        elif j == n+1:
            test_case[i].append(("target", j, a, b))
        else:
            test_case[i].append(("market", j, a, b))

for tc in test_case:
    visited = [False] * (len(tc))
    visited[0] = True
    q = deque()
    q.append(tc[0])
    is_happy = False
    while q:
        node, idx, y, x = q.popleft()
        if node == "target":
            print("happy")
            is_happy = True
            break
        else:
            # beer = 20
            for i in range(len(tc)):
                if not visited[i]:
                    dist = abs(y - tc[i][2]) + abs(x - tc[i][3])
                    if dist <= 1000:
                        q.append(tc[i])
                        visited[i] = True
    if not is_happy:
        print("sad")
