# 별찍기-10
import sys

N = int(sys.stdin.readline())
arr = [[0 for i in range(N)] for j in range(N)]


def drawPattern(array, x, y, size):
    N = size
    #print(N)
    if N > 3:
        boxN = int(N / 3)
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                drawPattern(array, x + boxN * i, y + boxN * j, boxN)
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                #print(x + i, y + j, x, y)
                array[x + i][y + j] = 1


drawPattern(arr, 0, 0, len(arr))

for i in arr:
    for j in i:
        if j == 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()
