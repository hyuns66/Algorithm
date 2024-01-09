# NBA 농구

import sys

N = int(sys.stdin.readline())

Ascore = 0
Bscore = 0
currentTeam = 0

Atimes = []
Btimes = []
for i in range(N):
    team, time = sys.stdin.readline().strip().split()
    if team == '1':
        Ascore += 1
    else:
        Bscore += 1

    if Ascore > Bscore:
        if currentTeam == 2 or currentTeam == 3:  # B팀이 이기고 있었거나 동점상황이었다면
            Atimes.append(time)
            currentTeam = 1
        elif currentTeam == 0:  # 첫 득점이면
            Atimes.append(time)
            currentTeam = 1
    elif Bscore > Ascore:
        if currentTeam == 1 or currentTeam == 3:  # A팀이 이기고 있었거나 동점상황이었다면
            Btimes.append(time)
            currentTeam = 2
        elif currentTeam == 0:  # 첫 득점이면
            Btimes.append(time)
            currentTeam = 2
    elif Ascore == Bscore:
        if currentTeam == 1:  # A팀이 이기고 있었다면
            Atimes.append(time)
            currentTeam = 3  # 동점상황 표시
        elif currentTeam == 2:  # B팀이 이기고 있었다면
            Btimes.append(time)
            currentTeam = 3  # 동점상황 표시


if currentTeam == 1:
    Atimes.append("48:00")
elif currentTeam == 2:
    Btimes.append("48:00")

#print(Atimes)
#print(Btimes)

if len(Atimes) != 0:
    d = 0
    for i in range(0, len(Atimes), 2):
        start = Atimes[i]
        end = Atimes[i + 1]

        startMin, startSec = map(int, start.split(":"))
        endMin, endSec = map(int, end.split(":"))

        startTotal = 60*startMin+startSec
        endTotal = 60*endMin+endSec

        duration = endTotal-startTotal
        d += duration
    dMin = d // 60
    dSec = d % 60
    print("{:02d}:{:02d}".format(dMin, dSec))
else:
    print("00:00")

if len(Btimes) != 0:
    d = 0
    for i in range(0, len(Btimes), 2):
        start = Btimes[i]
        end = Btimes[i + 1]

        startMin, startSec = map(int, start.split(":"))
        endMin, endSec = map(int, end.split(":"))

        startTotal = 60 * startMin + startSec
        endTotal = 60 * endMin + endSec

        duration = endTotal - startTotal
        d += duration
    dMin = d // 60
    dSec = d % 60
    print("{:02d}:{:02d}".format(dMin, dSec))
else:
    print("00:00")

# 런타임 에러(인덱스 에러)
# A팀 승리 -> 동점 상황-> A팀 다시 승리하는 상황을 고려하지 않았었다.
