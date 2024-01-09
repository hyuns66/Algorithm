import math
import sys

def isSquare(n : int):
    return int(math.sqrt(n)) ** 2 == n

N, M = map(int, sys.stdin.readline().split())
mat = [list() for i in range(N)]
max_num = -1

for i in range(N):
    mat[i] = list(sys.stdin.readline().rstrip())
    for j in range(M):
        mat[i][j] = int(mat[i][j])

for y in range(N):
    for x in range(M):  # 시작 위치
        for y_dir in range(-N+1, N):
            for x_dir in range(-M+1, M):    # 각 등차수열 계수에 대하여
                num = mat[y][x]
                if y_dir == 0 and x_dir == 0:
                    if isSquare(num) and max_num < num:
                        max_num = num
                    continue
                decimal = 10
                cur_x = x
                cur_y = y
                while True:
                    if 0 <= cur_y+y_dir < N and 0 <= cur_x+x_dir < M:
                        cur_y = cur_y+y_dir
                        cur_x = cur_x+x_dir
                        num += mat[cur_y][cur_x] * decimal
                        decimal *= 10
                        if isSquare(num) and max_num < num:
                            max_num = num
                    else:
                        break

print(max_num)