def backTracking(graph, positions, depth, answer, hy, hx):
    rry, rrx, bby, bbx = positions
    if depth == 10:
        return 11
    for dy, dx in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
        if dy == -hy and dx == -hx:
            continue
        ry = rry
        rx = rrx
        by = bby
        bx = bbx
        flag = False
        while graph[by+dy][bx+dx] != "#":
            by += dy
            bx += dx
            if graph[by][bx] == "O":
                flag = True
                break
        if flag:
            continue
        while graph[ry+dy][rx+dx] != "#":
            ry += dy
            rx += dx
            if graph[ry][rx] == "O":
                return min(answer, depth+1)
        if ry == rry and rx == rrx and by == bby and bx == bbx: # 변화없는 경우는 skip
            continue
        if ry == by and rx == bx:
            if rry*dy > bby*dy or rrx*dx > bbx*dx:
                by -= dy
                bx -= dx
            if rry*dy < bby*dy or rrx*dx < bbx*dx:
                ry -= dy
                rx -= dx
        answer = min(answer, backTracking(graph, [ry, rx, by, bx], depth+1, answer, dy, dx))
    return answer


N, M = map(int, input().split())
graph = list()
ry, rx = [0, 0]
by, bx = [0, 0]
for y in range(N):
    graph.append(list(input().rstrip()))
    for x, char in enumerate(graph[y]):
        if char == "R":
            ry = y
            rx = x
        if char == "B":
            by = y
            bx = x

answer = backTracking(graph, [ry, rx, by, bx], 0, 11, 0, 0)
print(answer if answer<=10 else -1)