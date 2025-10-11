from collections import deque
import sys

N, M, X = map(int, input().split())

inRoad = [[] for _ in range(N+1)]
outRoad = [[] for _ in range(N+1)]
for i in range(M):
    start, end, time = map(int, input().split())
    inRoad[end].append((start, time))
    outRoad[start].append((end, time))

inDist = [sys.maxsize for _ in range(N+1)]
outDist = [sys.maxsize for _ in range(N+1)]
q = deque()
q.append((X, 0))
while q:
    cur, time = q.pop()
    if outDist[cur] < time:
        continue
    for dest, nextTime in outRoad[cur]:
        if outDist[dest] <= time + nextTime:
            continue
        outDist[dest] = time + nextTime
        q.append((dest, time + nextTime))
q.clear()
q.append((X, 0))
while q:
    cur, time = q.pop()
    if inDist[cur] < time:
        continue
    for dest, nextTime in inRoad[cur]:
        if inDist[dest] <= time + nextTime:
            continue
        inDist[dest] = time + nextTime
        q.append((dest, time + nextTime))

maxTime = 0
for i in range(1, N+1):
    if i == X: continue
    totalTime = inDist[i] + outDist[i]
    maxTime = max(maxTime, totalTime)
print(maxTime)
