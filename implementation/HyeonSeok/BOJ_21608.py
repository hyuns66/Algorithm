import heapq

def find_seat(favorite, graph):
    global N
    h = list()
    for y in range(N):
        for x in range(N):
            if graph[y][x] != -1:
                continue
            favorite_count = 0
            empty_count = 0
            for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                py = y + dy
                px = x + dx
                if py < 0 or px < 0 or py >= N or px >= N:
                    continue
                if (graph[py][px] in favorite):
                    favorite_count += 1
                elif (graph[py][px] == -1):
                    empty_count += 1
            # 1, 2, 3 조건 순서대로 우선순위 매겨서 힙에 삽입
            heapq.heappush(h, (-favorite_count, -empty_count, y, x))
    return heapq.heappop(h)

N = int(input())
order = list()
favorites = [[] for _ in range(N ** 2)]
graph = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(N ** 2):
    nums = list(map(int, input().split()))
    student = nums[0] - 1
    order.append(student)
    for i in range(1, 5):
        favorites[student].append(nums[i]-1)
for child in order:
    _, _, y, x = find_seat(favorites[child], graph)
    graph[y][x] = child
answer = 0
for y in range(N):
    for x in range(N):
        child = graph[y][x]
        fc = 0
        for dy, dx in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            py = y + dy
            px = x + dx
            if py < 0 or px < 0 or py >= N or px >= N:
                continue
            if graph[py][px] in favorites[child]:
                fc += 1
        if fc == 0:
            continue
        answer += 10 ** (fc - 1)
print(answer)