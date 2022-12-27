import sys

N = int(sys.stdin.readline())
circles = [list() for i in range(N)]
points = list()

for i in range(N):
    circles[i] = list(map(int, sys.stdin.readline().split()))

for i in range(N):  # 시작점과 끝점의 조합으로 배열 바꿈
    start = circles[i][0] - circles[i][1]
    end = circles[i][0] + circles[i][1]
    circles[i] = [start, end]
    points.append([start, i])
    points.append([end, i])

points.sort(key=lambda x:x[0])
circles.sort(key=lambda x: x[0])
stack = list()

while len(points) != 0:
    if len(stack) == 0:
        stack.append(points.pop()[1])
        continue
    if stack[-1] == points[-1][1]:
        stack.pop()
        points.pop()
    else:
        stack.append(points.pop()[1])

if len(stack) == 0:
    print("YES")
else:
    print("NO")
