# 배열 돌리기1- 반시계방향으로

import sys

N, M, R = map(int, sys.stdin.readline().split())

arr = [[0 for j in range(M)] for i in range(N)]
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))

for _ in range(R):
    upLine, downLine, leftLine, rightLine = 0, N - 1, 0, M - 1
    while True:
        # print(f"{upLine}/{downLine}/{leftLine}/{rightLine}")

        tempZero = arr[upLine][leftLine]
        for i in range(rightLine - leftLine):  # 젤 윗줄 왼쪽으로 밀기
            arr[upLine][leftLine + i] = arr[upLine][leftLine + i + 1]
        for i in range(downLine - upLine):  # 젤 오른쪽줄 위로 밀기
            arr[upLine + i][rightLine] = arr[upLine + i + 1][rightLine]
        for i in range(rightLine - leftLine):  # 젤 아래쪽줄 오른쪽으로 밀기
            arr[downLine][rightLine - i] = arr[downLine][rightLine - i - 1]
        for i in range(downLine - upLine):  # 젤 왼쪽줄 아래로밀기
            arr[downLine - i][leftLine] = arr[downLine - i - 1][leftLine]
        arr[upLine + 1][leftLine] = tempZero

        upLine += 1
        downLine -= 1
        rightLine -= 1
        leftLine += 1
        if upLine >= downLine or leftLine >= rightLine:
            break

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()
