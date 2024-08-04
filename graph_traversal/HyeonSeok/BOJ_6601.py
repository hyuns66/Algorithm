import sys
from collections import deque

def bfs(sy, sx, desty, destx):
    q = deque()
    q.append((sy, sx, 0))
    visited = [[False for _ in range(8)] for _ in range(8)]
    visited[sy][sx] = True
    dir = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]
    while q:
        y, x, count = q.popleft()
        if y == desty and x == destx:
            return count
        for dy, dx in dir:
            py = y + dy
            px = x + dx
            if py < 0 or py >= 8 or px < 0 or px >= 8:
                continue
            if not visited[py][px]:
                visited[py][px] = True
                q.append((py, px, count+1))
                


lines = sys.stdin.readlines()
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for line in lines:
    start, dest = line.split()
    scol, srow = list(start)
    dcol, drow = list(dest)
    srow = int(srow)-1
    drow = int(drow)-1
    scol = cols.index(scol)
    dcol = cols.index(dcol)
    count = bfs(scol, srow, dcol, drow)
    print(f"To get from {start} to {dest} takes {count} knight moves.")
