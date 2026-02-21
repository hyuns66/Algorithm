import sys

# y, x 좌표로부터 해당 영역에 색종이를 둘 수 있는지 판단 (1만 덮어야 하므로)
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
    if depth == 100:    # 맨 끝까지 도착하면 answer 업데이트 (백트래킹 과정에서 불필요한 경우는 쳐냈기 때문에 검증하지 않아도 됨)
        temp = 0
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
            if not canCover(y, x, s[0]):    # 현재 색종로로 덮을 수 없는 경우 더 큰색종도도 용용지물이므로 break
                break
            for i in range(s[0]):       # 색종이로 덮고 backtracking
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
