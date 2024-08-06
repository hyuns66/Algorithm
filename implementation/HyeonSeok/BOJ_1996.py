N = int(input())
graph = list()
answer = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    graph.append(list(input()))
for y in range(N):
    for x in range(N):
        if graph[y][x] == ".":
            continue
        answer[y][x] = "*"
        for dy, dx in [[0, 1], [1, 1], [1, 0], [1 ,-1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            py = y + dy
            px = x + dx
            if py < 0 or py >= N or px < 0 or px >= N:
                continue
            if answer[py][px] == "M" or answer[py][px] == "*":
                continue
            answer[py][px] += int(graph[y][x])
            if answer[py][px] >= 10:
                answer[py][px] = "M"
for a in answer:
    for num in a:
        print(num, end="")
    print("")