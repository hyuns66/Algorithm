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

# 이미 다 익었는지 여부랑, 안익은 토마토 리스트 만들기
allRipe = True
notRipeList = []
for h in range(H):
    for n in range(N):
        for m in range(M):
            # print(f"?{h}:{n}:{m}")
            if boxes[h][n][m] == 0:  # 안 익은 토마토일때
                allRipe = False
                notRipeList.append([h, n, m])

# print(f"notRipeList: {notRipeList}")

if allRipe:
    print(0)
else:
    day = 0
    while True:
        willRipeList = []
        newNotRipeList = []
        if len(notRipeList) == 0:
            print(day)
            break

        flagEndNow = False
        for t in notRipeList:
            # for b in boxes:
            #     for r in b:
            #         print(r)
            # print(f"**** {t[0]}, {t[1]}, {t[2]} ***** 검사중")
            flag = False  # 주위에 토마토가 있는지 여부
            yeahFlag = False

            if (t[0] + 1) < H and boxes[t[0] + 1][t[1]][t[2]] == 1:
                # print(f"상에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                # print(f"**** 상 {t[0] + 1}, {t[1]}, {t[2]} 에 익토 있음 /{boxes[t[0] + 1][t[0]][t[2]]} *****")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[0] + 1) < H and boxes[t[0] + 1][t[1]][t[2]] == 0:
                # print(f"**** 상 {t[0] + 1}, {t[1]}, {t[2]} 에 안익토 있음/{boxes[t[0] + 1][t[1]][t[2]]} /? boxes[1][1][2] = {boxes[1][1][2]}*****")
                flag = True

            if (t[0] - 1) >= 0 and boxes[t[0] - 1][t[1]][t[2]] == 1:
                # print(f"하에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                # print(f"**** 하 {t[0] - 1}, {t[1]}, {t[2]} 에 익토 있음 /{boxes[t[0] - 1][t[0]][t[2]]}*****")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[0] - 1) >= 0 and boxes[t[0] - 1][t[1]][t[2]] == 0:
                # print(f"**** 하 {t[0] - 1}, {t[1]}, {t[2]} 에 안익토 있음 /{boxes[t[0] - 1][t[0]][t[2]]}*****")
                flag = True

            if (t[1] + 1) < N and boxes[t[0]][t[1] + 1][t[2]] == 1:
                # print(f"아래에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                # print(f"**** 아래 {t[0]}, {t[1] + 1}, {t[2]} 에 익토 있음 /{boxes[t[0]][t[1] + 1][t[2]]}*****")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[1] + 1) < N and boxes[t[0]][t[1] + 1][t[2]] == 0:
                # print(f"**** 아래 {t[0]}, {t[1] + 1}, {t[2]} 에 안익토 있음 /{boxes[t[0]][t[1] + 1][t[2]]}*****")
                flag = True

            if (t[1] - 1) >= 0 and boxes[t[0]][t[1] - 1][t[2]] == 1:
                # print(f"위에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                # print(f"**** 위 {t[0]}, {t[1] - 1}, {t[2]} 에 익토 있음 /{boxes[t[0]][t[1] - 1][t[2]]}*****")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[1] - 1) >= 0 and boxes[t[0]][t[1] - 1][t[2]] == 0:
                # print(f"**** 위 {t[0]}, {t[1] - 1}, {t[2]} 에 안익토 있음 /{boxes[t[0]][t[1] - 1][t[2]]}*****")
                flag = True

            if (t[2] + 1) < M and boxes[t[0]][t[1]][t[2] + 1] == 1:
                # print(f"우에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                # print(f"**** 우 {t[0]}, {t[1]}, {t[2] + 1} 에 익토 있음 /{boxes[t[0]][t[1]][t[2] + 1] }*****")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[2] + 1) < M and boxes[t[0]][t[1]][t[2] + 1] == 0:
                # print(f"**** 우 {t[0]}, {t[1]}, {t[2] + 1} 에 안익토 있음 /{boxes[t[0]][t[1]][t[2] + 1] }*****")
                flag = True

            if (t[2] - 1) >= 0 and boxes[t[0]][t[1]][t[2] - 1] == 1:
                # print(f"좌에 익토 : {t[0]}, {t[1]}, {t[2]} 추가됨.")
                # print(f"**** 좌 {t[0]}, {t[1]}, {t[2] - 1} 에 익토 있음 /{boxes[t[0]][t[1]][t[2] - 1] }*****")
                willRipeList.append([t[0], t[1], t[2]])
                flag = True
                yeahFlag = True
            elif (t[2] - 1) >= 0 and boxes[t[0]][t[1]][t[2] - 1] == 0:
                # print(f"**** 좌 {t[0]}, {t[1]}, {t[2] - 1} 에 안익토 있음 /{boxes[t[0]][t[1]][t[2] - 1] }*****")
                flag = True

            if not yeahFlag:
                newNotRipeList.append(t)
            if not flag:  # 상하좌우위아래에 토마토가 없으면, 절대 익지 않으므로,
                print(-1)
                flagEndNow = True
                # print("break됨")
                break

        notRipeList = newNotRipeList
        if flagEndNow:
            break

        day += 1
        # print(f"willRipeList: {willRipeList}")
        for t in willRipeList:
            boxes[t[0]][t[1]][t[2]] = 1

        # for r in boxes:
        #     for s in r:
        #         print(s)
        # print("---------------")
        # print(f"days:{day}")

# 뭔가 notRipeList를 for t in notRipeList하는 도중에 변경하니까 뭔가 잘 안됐다.


# 이 코드는 시간복잡도가 매우 높기 때문에 시간초과가 발생할 수 있습니다. 주어진 상자의 크기가 최대 100 x 100 x 100 이므로, 최악의 경우에는 최대 100,000,000개의 칸이 존재하게 됩니다.
# 이 코드에서는 매 회차마다 모든 칸을 탐색하고, 주변에 익은 토마토가 있는지 검사하는데, 이 작업이 매우 비효율적입니다. 따라서 이 문제를 효율적으로 해결하기 위해서는 BFS (Breadth-First
# Search) 알고리즘을 사용하면 됩니다. BFS를 사용하면 익은 토마토를 시작으로 탐색을 하면서, 거리가 1인 위치들을 모두 방문하게 되고, 그 다음에 거리가 2인 위치들을 방문하면서, 거리가 3, 4,
# ... 인 위치들을 방문하게 됩니다. 이렇게 BFS를 사용하면 시간복잡도는 O(NM)이 됩니다. 따라서 최대 100 x 100 x 100 크기의 상자에서도 충분히 빠르게 동작할 수 있습니다.
