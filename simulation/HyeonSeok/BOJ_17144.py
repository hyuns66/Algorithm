import sys
from collections import deque
import copy

def simulation(graph, cleaner, Y, X):
    new_graph = copy.deepcopy(graph)    # 2차원 그래프 부터는 얕은복사를 해도 각 열에 해당되는 객체는 복사되지 않는 문제점 해결위해 deepcopy 사용
    # 먼지 확산
    for y in range(Y):
        for x in range(X):
            if graph[y][x] <= 0:
                continue
            small_dust = graph[y][x] // 5
            for diry, dirx in [[0,1], [1,0], [-1,0], [0,-1]]:
                if y+diry >= Y or y+diry < 0 or x+dirx >= X or x+dirx < 0:
                    continue
                tary, tarx = y+diry, x+dirx
                if graph[tary][tarx] == -1:
                    continue
                new_graph[y][x] -= small_dust
                new_graph[tary][tarx] += small_dust
                
    # 공기순환
    for y in range(cleaner[0]-1, -1, -1):   # 공기청정기쪽으로 들어오는 순환
        new_graph[y+1][0] = new_graph[y][0]
    for y in range(cleaner[1]+2, Y):
        new_graph[y-1][0] = new_graph[y][0]
    for y in [0, -1]:   # 최상단, 최하단 좌측순환
        temp = deque(new_graph[y])
        temp.rotate(-1)
        new_graph[y] = list(temp)
    for i in range(2):  # 상, 하 순환 i == 0 일 때가 상승 1일 때가 하강
        c = cleaner[i]
        if i == 0:
            for y in range(1, c+1):
                new_graph[y-1][-1] = new_graph[y][-1]
        if i == 1:
            for y in range(Y-2, c-1, -1):
                new_graph[y+1][-1] = new_graph[y][-1]
    for y in cleaner:   # 중단 우측순환
        temp = deque(new_graph[y])
        temp.rotate(1)
        temp[0] = -1
        temp[1] = 0
        new_graph[y] = list(temp)
    return new_graph


R, C, T = map(int, sys.stdin.readline().split())
graph = [0 for _ in range(R)]
cleaner = []

for i in range(R):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    if graph[i][0] == -1:
        cleaner.append(i)   # 공기청정기 y좌표
    
for t in range(T):
    graph = simulation(graph, cleaner, R, C).copy()
    
answer = 0
for row in graph:
    # print(*row)
    for value in row:
        if value == -1:
            continue
        answer+=value

print(answer)