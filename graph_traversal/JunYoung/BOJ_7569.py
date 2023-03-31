# 토마토
# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸

# import sys
#
# M, N, H = map(int, sys.stdin.readline().split())  # 가로, 세로, 높이
#
# boxes = []
# for _ in range(H):
#     boxes.append([0 for m in range(M)] for n in range(N))
#
# for h in range(H):
#     for n in range(N):
#         print(n)
#         print(list(map(int, sys.stdin.readline().strip().split())))
#
# print(boxes)

import sys

M, N, H = map(int, sys.stdin.readline().split())  # 가로, 세로, 높이

boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().strip().split())))
    boxes.append(box)

# print(boxes)

allRipe = True
notRipeList = []
for h in range(H):
    for m in range(M):
        for n in range(N):
            # print(f"?{h}:{n}:{m}")
            if boxes[h][n][m] == 0:  # 안 익은 토마토일때
                allRipe = False
                notRipeList.append([h, n, m])

if allRipe:
    print(0)
else:
    day = 0
    while True:
        willRipeList = []
        if len(notRipeList) == 0:
            print(day)
            break

        flagEndNow = False
        for t in notRipeList:
            flag = False  # 주위에 토마토가 있는지 여부
            yeahFlag = False

            if (t[0] + 1) < H and boxes[t[0] + 1][t[0]][t[2]] == 1:
                print(f"상에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[0] + 1) < H and boxes[t[0] + 1][t[0]][t[2]] == 0:
                flag = True

            if (t[0] - 1) >= 0 and boxes[t[0] - 1][t[0]][t[2]] == 1:
                print(f"하에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[0] - 1) >= 0 and boxes[t[0] - 1][t[0]][t[2]] == 0:
                flag = True

            if (t[1] + 1) < N and boxes[t[0]][t[1] + 1][t[2]] == 1:
                print(f"아래에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[1] + 1) < N and boxes[t[0]][t[1] + 1][t[2]] == 0:
                flag = True

            if (t[1] - 1) >= 0 and boxes[t[0]][t[1] - 1][t[2]] == 1:
                print(f"위에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[1] - 1) >= 0 and boxes[t[0]][t[1] - 1][t[2]] == 0:
                flag = True

            if (t[2] + 1) < M and boxes[t[0]][t[1]][t[2] + 1] == 1:
                print(f"우에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[2] + 1) < M and boxes[t[0]][t[1]][t[2] + 1] == 0:
                flag = True

            if (t[2] + 1) >= 0 and boxes[t[0]][t[1]][t[2] - 1] == 1:
                print(f"좌에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[2] + 1) >= 0 and boxes[t[0]][t[1]][t[2] - 1] == 0:
                flag = True

            if yeahFlag:
                notRipeList.remove(t)
            if not flag:  # 상하좌우위아래에 토마토가 없으면, 절대 익지 않으므로,
                print(-1)
                flagEndNow = True
                break

        if flagEndNow:
            break

        day += 1
        print(willRipeList)
        for t in willRipeList:
            boxes[t[0]][t[1]][t[2]] = 1

        for r in boxes:
            for s in r:
                print(s)
        print("---------------")
        print(f"days:{day}")
