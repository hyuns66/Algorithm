# 달팽이

import sys

N = int(sys.stdin.readline())
targetNum = int(sys.stdin.readline())
arr = [[0 for j in range(N)] for i in range(N)]

snail = 1
step = 0  # 0이면 위로, 1이면 오른쪽, 2이면 아래로, 3면 아래로
indexX, indexY = int((N + 1) / 2) - 1, int((N + 1) / 2) - 1  # index값이라 -1해줌.
maxUp, maxDown, maxLeft, maxRight = int((N + 1) / 2) - 1, int((N + 1) / 2) - 1, int((N + 1) / 2) - 1, int(
    (N + 1) / 2) - 1

arr[indexY][indexX] = snail
snail += 1

while True:
    if snail == N * N + 1:
        break

    if step == 4:
        step = 0

    # 위치 이동
    if step == 0:  # 위
        indexY -= 1
        if indexY < maxUp - 1:
            step += 1
            indexY += 1
            maxUp = indexY
            continue
    elif step == 1:  # 오른쪽
        indexX += 1
        if indexX > maxRight + 1:
            step += 1
            indexX -= 1
            maxRight = indexX
            continue
    elif step == 2:  # 아래
        indexY += 1
        if indexY > maxDown + 1:
            step += 1
            indexY -= 1
            maxDown = indexY
            continue
    else:  # 왼쪽
        indexX -= 1
        if indexX < maxLeft - 1:
            step += 1
            indexX += 1
            maxLeft = indexX
            continue

    arr[indexY][indexX] = snail
    # print(f"{indexY}, {indexX}에 {snail} 값 넣음")
    snail += 1

answer = []
for i in range(N):
    for j in range(N):
        if targetNum == arr[i][j]:
            answer.append(i + 1)
            answer.append(j + 1)

for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()

for i in answer:
    print(i, end=' ')

# 파이썬에는 switch case문이 없다는 사실!
