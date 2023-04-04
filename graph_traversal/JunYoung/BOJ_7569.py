# 토마토

import sys

M, N, H = map(int, sys.stdin.readline().split())  # 가로, 세로, 높이

boxes = []
for _ in range(H):
    box = []
    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().strip().split())))
    boxes.append(box)

# 이미 다 익었는지 여부랑, 익은 토마토 리스트 만들기
notRipeTomatoNum = 0
ripeTomatoList = []
for h in range(H):
    for n in range(N):
        for m in range(M):
            # print(f"?{h}:{n}:{m}")
            if boxes[h][n][m] == 1:  # 익은 토마토일때
                ripeTomatoList.append([h, n, m])
            elif boxes[h][n][m] == 0:
                notRipeTomatoNum += 1

# print(f"notRipeList: {notRipeList}")

if notRipeTomatoNum == 0:
    print(0)
else:
    day = 0
    while True:
        if notRipeTomatoNum == 0:
            print(day)
            break
        elif len(ripeTomatoList) == 0: # 안익은 토마토가 남았느데 익힐 토마토가 없다면 땡~
            print(-1)
            break

        nextRipeList = []
        #print(f"ripeTomatoList: {ripeTomatoList} 주위 토마토 익힐 예정")
        for t in ripeTomatoList:
            if (t[0] + 1) < H and boxes[t[0] + 1][t[1]][t[2]] == 0:
                boxes[t[0] + 1][t[1]][t[2]] = 1
                notRipeTomatoNum -= 1
                nextRipeList.append([t[0] + 1, t[1], t[2]])
            if (t[0] - 1) >= 0 and boxes[t[0] - 1][t[1]][t[2]] == 0:
                boxes[t[0] - 1][t[1]][t[2]] = 1
                notRipeTomatoNum -= 1
                nextRipeList.append([t[0] - 1, t[1], t[2]])
            if (t[1] + 1) < N and boxes[t[0]][t[1] + 1][t[2]] == 0:
                boxes[t[0]][t[1] + 1][t[2]] = 1
                notRipeTomatoNum -= 1
                nextRipeList.append([t[0], t[1] + 1, t[2]])
            if (t[1] - 1) >= 0 and boxes[t[0]][t[1] - 1][t[2]] == 0:
                boxes[t[0]][t[1] - 1][t[2]] = 1
                notRipeTomatoNum -= 1
                nextRipeList.append([t[0], t[1] - 1, t[2]])
            if (t[2] + 1) < M and boxes[t[0]][t[1]][t[2] + 1] == 0:
                boxes[t[0]][t[1]][t[2] + 1] = 1
                notRipeTomatoNum -= 1
                nextRipeList.append([t[0], t[1], t[2] + 1])
            if (t[2] - 1) >= 0 and boxes[t[0]][t[1]][t[2] - 1] == 0:
                boxes[t[0]][t[1]][t[2] - 1] = 1
                notRipeTomatoNum -= 1
                nextRipeList.append([t[0], t[1], t[2] - 1])

        day += 1
        ripeTomatoList = nextRipeList

        # print(f"****{day}일차****")
        # for i in boxes:
        #     for r in i:
        #         print(r)


# cf. set안에는 list가 못 들어간다.
# bfs 이용
