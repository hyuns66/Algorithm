# 상어 초등학교

import sys
from collections import deque


def calculateHappy(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x == 2:
        return 10
    elif x == 3:
        return 100
    elif x == 4:
        return 1000


N = int(sys.stdin.readline())
arr = [[0 for j in range(N)] for i in range(N)]

favorites = {}
for num in range(1, N * N + 1):  # N*N명의 학생을 배치하려고한다.
    temp = list(map(int, sys.stdin.readline().strip().split()))
    student = temp[0]
    favorite = temp[1:]
    favorites[student] = favorite

    # if num == N * N:
    #     print(f"마지막 {num} 도달")
    #     flag = False
    #     for i in range(N):
    #         for j in range(N):
    #             if arr[i][j] == 0:
    #                 arr[i][j] = student
    #                 flag = True
    #                 break
    #         if flag == True:
    #             break
    #     break

    maxCountList = [0]
    # 각 자리를 보면서
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                continue  # 이미 차있는 자리니까 못들어간다.
            close = deque()
            emptySeatCount = 0
            if i + 1 < N:
                close.append(arr[i + 1][j])  # 아래
                if arr[i + 1][j] == 0:
                    emptySeatCount += 1
            if i - 1 >= 0:
                close.append(arr[i - 1][j])  # 위
                if arr[i - 1][j] == 0:
                    emptySeatCount += 1
            if j + 1 < N:
                close.append(arr[i][j + 1])  # 우측
                if arr[i][j + 1] == 0:
                    emptySeatCount += 1
            if j - 1 >= 0:
                close.append(arr[i][j - 1])  # 좌측
                if arr[i][j - 1] == 0:
                    emptySeatCount += 1

            count = 0
            for friend in favorite:
                if friend in close:
                    count += 1

            if maxCountList[0] < count:  # 최고값 갱신
                maxCountList.clear()
                maxCountList.append(count)
                maxCountList.append([i, j, emptySeatCount])
            elif maxCountList[0] == count:  # 최고값 추가
                maxCountList.append([i, j, emptySeatCount])

    # 학생의 자리 배정
    # print(f"maxCountList: {maxCountList}")
    if len(maxCountList) == 2:  # 1. 좋아하는 학생이 인접한 칸에 가장 많은 칸이 하나면,
        arr[maxCountList[1][0]][maxCountList[1][1]] = student
        #print(f"{num}번째 / 케이스1: {maxCountList[1][0]},{maxCountList[1][1]}에 {student} 배치")
    else:  # 좋아하는 학생이 인접한 칸에 가장 많은 칸이 여러개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정함.
        maxEmpty = [0]
        for i in range(1, len(maxCountList)):
            if maxCountList[i][2] > maxEmpty[0]:
                maxEmpty.clear()
                maxEmpty.append(maxCountList[i][2])
                maxEmpty.append([maxCountList[i][0], maxCountList[i][1]])
            elif maxCountList[i][2] == maxEmpty[0]:
                maxEmpty.append([maxCountList[i][0], maxCountList[i][1]])

        # print(f"maxEmpty: {maxEmpty}")
        if len(maxEmpty) == 2:  # 2. 인접한 칸 중에 비어있는 칸이 가장 많은 자리가 하나면,
            arr[maxEmpty[1][0]][maxEmpty[1][1]] = student
            #print(f"{num}번째 / 케이스2: {maxCountList[1][0]},{maxCountList[1][1]}에 {student} 배치")
        else:  # 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
            # 근데 이미 maxEmpty에 넣을때, i,j가 작은 순으로 들어가 있기 때문에 코드는 같다.
            arr[maxEmpty[1][0]][maxEmpty[1][1]] = student
            #print(f"{num}번째 / 케이스3: {maxCountList[1][0]},{maxCountList[1][1]}에 {student} 배치")

# for i in range(N):
#     print(arr[i])

index = 0
totalHappy = 0
for i in range(N):
    for j in range(N):
        close = []
        if i + 1 < N:
            close.append(arr[i + 1][j])  # 아래
        if i - 1 >= 0:
            close.append(arr[i - 1][j])  # 위
        if j + 1 < N:
            close.append(arr[i][j + 1])  # 우측
        if j - 1 >= 0:
            close.append(arr[i][j - 1])  # 좌측

        count = 0
        for friend in favorites[arr[i][j]]:
            if friend in close:
                count += 1

        totalHappy += calculateHappy(count)
        #print(f"{index + 1}번째: {arr[i][j]}의 만족도가 {calculateHappy(count)} 추가됨")
        #print(f"{favorites[arr[i][j]]} / {close} / {count}")
        index += 1

print(totalHappy)
