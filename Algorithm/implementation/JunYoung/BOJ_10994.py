# 별 찍기- 19

import sys

N = int(sys.stdin.readline())

cols = (1 + 4 * (N - 1))
arr = [[' ' for j in range(1 + 4 * (N - 1))] for i in range(1 + 4 * (N - 1))]

start = 0
end = cols - 1
for t in range(N):
    for i in range(cols):
        arr[start][start + i] = '*'  # 왼쪽세로
        arr[end][start + i] = '*'  # 오른쪽세로
        arr[start + i][start] = '*'  # 위쪽가로
        arr[start + i][end] = '*'  # 아래쪽가로
    # print(str(start) + "/ " + str(end))
    cols -= 4
    start += 2
    end -= 2

for i in range(len(arr)):
    for j in arr[i]:
        print(j, end='')
    print('')

#리스트 2차원 배열