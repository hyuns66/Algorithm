import sys

def canCover(y, x, width):
    global graph
    for i in range(width):
        for j in range(width):
            if graph[y+i][x+j] != 1:
                return False
    return True

def backTracking(depth):
    global graph, squares, answer
    y = depth // 10
    x = depth % 10
    if depth == 100:
        temp = 0
        for y in range(10):
            for x in range(10):
                if graph[y][x] == 1:
                    return
        for s in squares:
            temp += (5 - s[1])
        answer = min(answer, temp)
        return
    if graph[y][x] == 1:
        for s in squares:
            if y+s[0]-1 >= 10 or x+s[0]-1 >= 10:  # 색종이가 그래프 넘어가는 경우 제외
                break
            if s[1] == 0:   # 해당 색종이 이미 다썼으면 continue
                continue
            if not canCover(y, x, s[0]):
                continue
            for i in range(s[0]):
                for j in range(s[0]):
                    graph[y+i][x+j] = 0
            s[1] -= 1
            backTracking(depth+1)
            s[1] += 1
            for i in range(s[0]):
                for j in range(s[0]):
                    graph[y+i][x+j] = 1
    else:
        backTracking(depth+1)
    
answer = sys.maxsize
squares = list()
for i in range(1, 6):
    temp = [i, 5]
    squares.append(temp)
graph = list()
for _ in range(10):
    temp = list(map(int, sys.stdin.readline().split()))
    graph.append(temp)
    
backTracking(0)
print(answer if answer != sys.maxsize else -1)
