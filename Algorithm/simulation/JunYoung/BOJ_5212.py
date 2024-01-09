#지구 온난화
import sys

R, C = map(int, sys.stdin.readline().split())

map = []
for i in range(R):
    line = sys.stdin.readline().strip()
    map.append([0 if char == '.' else 1 for char in line])

disland = []
for i in range(R):
    for j in range(C):
        if map[i][j] == 1:
            count = 0
            if (i - 1) >= 0 and map[i - 1][j] == 0:
                count += 1
            if (i + 1) <= (R - 1) and map[i + 1][j] == 0:
                count += 1
            if (j - 1) >= 0 and map[i][j - 1] == 0:
                count += 1
            if (j + 1) <= (C - 1) and map[i][j + 1] == 0:
                count += 1

            # 지도에 안 나온 곳은 바다다!
            if (i - 1) < 0:
                count += 1
            if (j - 1) < 0:
                count += 1
            if (i + 1) >= R:
                count += 1
            if (j + 1) >= C:
                count += 1

            if count >= 3:
                disland.append([i, j])  # 없어진다.

#print(disland)

for i in disland:
    map[i[0]][i[1]] = 0

minx = sys.maxsize
maxx = -1
miny = sys.maxsize
maxy = -1
for i in range(R):
    for j in range(C):
        if map[i][j] == 1:
            if i < miny:
                miny = i
            if i > maxy:
                maxy = i
            if j < minx:
                minx = j
            if j > maxx:
                maxx = j

# print(map)

#print(minx, maxx)
#print(miny, maxy)

for i in range(miny, min(R, maxy + 1)):
    for j in range(minx, min(C, maxx + 1)):
        if map[i][j] == 1:
            print("X", end='')
        else:
            print(".", end='')
    print()

# 더 좋은 풀이?
