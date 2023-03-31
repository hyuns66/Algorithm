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


#print(boxes)

allRipe = True
notRipeList = []
for h in range(H):
    for m in range(M):
        for n in range(N):
            #print(f"?{h}:{n}:{m}")
            if boxes[h][n][m] == -1:  # 안 익은 토마토일때
                allRipe = False
                notRipeList.append([h, n, m])

if allRipe:
    print(0)
else:
    day = 0
    while True:
        willRipeList = []
        if len(notRipeList) ==0:
            print(day)
            break

        flagEndNow = False
        for t in notRipeList:
            flag = False # 주위에 토마토가 있는지 여부
            for i in (-1, 1):
                for j in (-1, 1):
                    for k in (-1, 1):
                        if t[0] + i <0 or t[0] + i> H-1 or t[0] + i <0 or t[0] + i > N-1 or t[2] + k<0 or t[2] + k > M-1:
                            break
                        if boxes[t[0] + i][t[0] + i][t[2] + k] == 1:  # 상화좌우위아래에 익은 토마토가 있다면,
                            willRipeList.append([t[0], t[1], t[2]])
                            notRipeList.remove(t)
                            flag = True
                        elif boxes[t[0] + i][t[1] + j][t[2] + k] == 1:
                            flag = True
            if not flag:  # 상하좌우위아래에 토마토가 없으면, 절대 익지 않으므로,
                print(-1)
                flagEndNow = True
                break

        if flagEndNow:
            break

        day += 1
        for t in willRipeList:
            boxes[t[0] + i][t[1] + j][t[2] + k] == 1

