# 도영이가 만든 맛있는 음식

import sys
import itertools

N = int(sys.stdin.readline())

foodList = []
for i in range(N):
    S, B = map(int, sys.stdin.readline().split())
    food = [S, B]
    foodList.append(food)

cookFoodList = []
for j in range(2, N+1):
    # print(j)
    foodComb = list(itertools.combinations(foodList, j))
    # print("foodComb", end='')
    # print(foodComb)

    for fc in foodComb:
        sour = 1
        bitter = 0
        for f in fc:
            # print(fc)
            # print("속의")
            # print(f)

            sour *= f[0]
            bitter += f[1]
        # print(sour, end='/')
        # print(bitter, end='')
        # print(" 추가됨.")
        cookFoodList.append([sour, bitter])

for j in cookFoodList:
    foodList.append(j)

# print(foodList)

diffList = []
for i in range(len(foodList)):
    diff = foodList[i][1] - foodList[i][0]
    diffList.append(abs(diff))

diffList.sort()
print(diffList[0])
