def rotate_tetro(tetro):
    for _ in range(4):
        for i, pos in enumerate(tetro):
            y, x = pos
            tetro[i] = [-x, y]
        yield tetro
        for i, pos in enumerate(tetro):
            y, x = pos
            tetro[i] = [y, -x]
        yield tetro
        for i, pos in enumerate(tetro):
            y, x = pos
            tetro[i] = [y, -x]

N, M = map(int, input().split())
graph = list()
for _ in range(N):
    graph.append(list(map(int, input().split())))
tetros = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 1]]
        ]
answer = 0
for y in range(N):
    for x in range(M):
        for tetro in tetros:
            for tet in rotate_tetro(tetro):
                num = 0
                for dy, dx in tet:
                    py = y+dy
                    px = x+dx
                    if py < 0 or py >= N or px < 0 or px >= M:
                        num = 0
                        break
                    num += graph[py][px]
                answer = max(answer, num)
print(answer)