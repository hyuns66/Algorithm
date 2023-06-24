# Z

import sys

N, r, c = map(int, sys.stdin.readline().split())
#arr = [[0 for i in range(2**N)] for j in range(2**N)]
count = 0


def visit(x, y, size):
    global count

    if size > 2:
        if not (x <= r < x + size and y <= c < y + size):
            count += size * size
            return
        else:
            size = int(size / 2)
            for i in range(2):
                for j in range(2):
                    # print("size", size)
                    # print(x + size * i, y + size * j)
                    visit(x + size * i, y + size * j, size)

    else:
        for i in range(2):
            for j in range(2):
                if x+i == r and y+j == c:
                    print(count)
                #array[x + i][y + j] = count
                count += 1


visit(0, 0, 2**N)

#print(arr[r][c])

# 메모리 초과 => 배열을 굳이 사용하지 않아도 됨
# 시간 초과 => 각 사분면을 다 탐색하지 않아도 됨
# x <= r < x + size and y <= c < y + size => 파이썬에선 이런 식으로 표기 가능하구나.
