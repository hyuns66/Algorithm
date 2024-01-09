# 치킨 배달

import sys
from itertools import combinations
gcityChicken = sys.maxsize

def calculateCityChicken(arr):
    global gcityChicken
    cityChicken = 0
    for i in range(N):
        for j in range(N):
            # 치킨거리 계산
            if arr[i][j] == 1:
                min = sys.maxsize
                for s in range(N):
                    for t in range(N):
                        if arr[s][t] == 2:
                            if abs(i - s) + abs(j - t) < min:
                                min = abs(i - s) + abs(j - t)
                cityChicken += min
                if cityChicken>=gcityChicken:
                    break
        if cityChicken >= gcityChicken:
            break
    return cityChicken

N, M = map(int, sys.stdin.readline().split())
arr = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    line = list(sys.stdin.readline().split())
    for j in range(len(line)):
        arr[i][j] = int(line[j])

homeList = []
storeList = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            homeList.append([i+1, j+1])
        elif arr[i][j] == 2:
            storeList.append([i+1, j+1])

possibleChoice = list(combinations(storeList, M))
#print(possibleChoice)

for stores in possibleChoice:
    arr2 = [[0 for i in range(N)] for j in range(N)]
    for h in homeList:
        arr2[h[0]-1][h[1]-1] = 1
    for s in stores:
        arr2[s[0] - 1][s[1] - 1] = 2
    result = calculateCityChicken(arr2)
    if result<gcityChicken:
        gcityChicken = result
    #print(result, gcityChicken)
print(gcityChicken)
