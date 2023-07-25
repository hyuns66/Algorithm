# 빗물

import sys

H, W = map(int, sys.stdin.readline().split())
blocks = list(map(int, sys.stdin.readline().split()))

dimension = [[0 for i in range(W)] for j in range(H)]

for i in range(len(blocks)):
    bnum = blocks[i]
    for j in range(bnum):
        dimension[H-1-j][i] = 1

#print(dimension)

totalRain = 0
for i in range(H):
    array = []
    for j in range(W):
        if dimension[i][j] == 1:
            array.append(j)
    #print(array)

    if len(array) >= 1:
        rain = (array[-1] - array[0] + 1) - len(array)
        totalRain += rain

print(totalRain)
