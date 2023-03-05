import sys

def make_square(step):
    global graph, center
    if step == 1:
        graph[center][center] = '*'
        return graph
    else:
        window = 2*(step-1)
        for y in range(center - window, center + window + 1):
            for x in range(center - window, center + window + 1):
                if y == center - window or y == center + window or x == center - window or x == center + window:
                    graph[y][x] = '*'
        step -= 1
        make_square(step)

N = int(sys.stdin.readline())
size = 4*(N-1) + 1
center = size // 2
graph = [[' ' for i in range(size)] for _ in range(size)]
make_square(N)

for g in graph:
    for char in g:
        print(char, end='')
    print("")