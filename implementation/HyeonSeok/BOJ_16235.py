def grow_and_die(tree, graph):
    die_tree = list()
    for y in range(len(tree)):
        for x in range(len(tree)):
            tree[y][x].sort(key = lambda x : x)
            idx = 0
            for i, age in enumerate(tree[y][x]):
                if graph[y][x] >= age:
                    graph[y][x] -= age
                    tree[y][x][i] += 1
                    idx += 1
                else:
                    break
            die_tree = tree[y][x][idx:]
            tree[y][x] = tree[y][x][:idx]
            while die_tree:
                age = die_tree.pop()
                graph[y][x] += age//2

def make_baby(tree, graph):
    for y in range(len(tree)):
        for x in range(len(tree)):
            for age in tree[y][x]:
                if age % 5 != 0:
                    continue
                for dy, dx in [[-1, -1,], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]:
                    py = y+dy
                    px = x+dx
                    if py < 0 or py >= len(graph) or px < 0 or px >= len(graph):
                        continue
                    tree[py][px].append(1)

def add_food(graph, additional_food):
    for y in range(len(graph)):
        for x in range(len(graph)):
            graph[y][x] += additional_food[y][x]

N, M, K = map(int, input().split())
additional_food = list()
graph = list()
tree = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    additional_food.append(list(map(int, input().split())))
    graph.append([5 for _ in range(N)])
for _ in range(M):
    y, x, age = map(int, input().split())
    tree[y-1][x-1].append(age)
for _ in range(K):
    grow_and_die(tree, graph)
    make_baby(tree, graph)
    add_food(graph, additional_food)
answer = 0
for y in range(len(tree)):
    for x in range(len(tree)):
        answer += len(tree[y][x])
print(answer)