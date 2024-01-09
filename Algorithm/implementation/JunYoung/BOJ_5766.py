# 할아버지는 유명해! 

import sys

totalAnswer = []
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    playerDict = {}
    for _ in range(N):
        ranking = list(map(int, sys.stdin.readline().split()))
        for player in ranking:
            if player in playerDict:
                playerDict[player] += 1
            else:
                playerDict[player] = 1

    playerDict = dict(sorted(playerDict.items(), key=lambda x: x[1], reverse=True))  # value를 기준으로 내림차순 정렬
    secondNum = list(playerDict.values())[1]

    answer = []
    for player in playerDict.keys():
        if playerDict[player] == secondNum:
            answer.append(player)
        elif playerDict[player] < secondNum:
            break

    answer.sort()
    for i in answer:
        totalAnswer.append(str(i) + ' ')
    totalAnswer.append('\n')

for i in totalAnswer:
    print(i, end='')

# playerDict = dict(sorted(playerDict.items(), key=lambda x: x[1], reverse=True))  # value를 기준으로 내림차순 정렬
# 숫자를 str으로 바꿔놓고 sort()하면 생각대로 소팅이 안된다.
