# ZOAC 3

import sys

leftHand = [
    ['q', 'w', 'e', 'r', 't']
    , ['a', 's', 'd', 'f', 'g']
    , ['z', 'x', 'c', 'v']
]

rightHand = [
    ['', 'y', 'u', 'i', 'o', 'p'],
    ['', 'h', 'j', 'k', 'l'],
    ['b', 'n', 'm']
]

leftAlphaLoc = {}
rightAlphaLoc = {}
for i in range(len(leftHand)):
    for j in range(len(leftHand[i])):
        leftAlphaLoc[leftHand[i][j]] = [i, j]
for i in range(len(rightHand)):
    for j in range(len(rightHand[i])):
        rightAlphaLoc[rightHand[i][j]] = [i, j]

sl, sr = map(str, sys.stdin.readline().split())
results = sys.stdin.readline().strip()

totalTime = 0
slLoc = leftAlphaLoc[sl]
srLoc = rightAlphaLoc[sr]
for i in results:
    if i in leftAlphaLoc:
        loc = leftAlphaLoc[i]
        leftTime = abs(loc[0] - slLoc[0]) + abs(loc[1] - slLoc[1])
        slLoc = loc
        totalTime += leftTime
        #print(f"{i} 누르러 왼쪽이 감: {leftTime}추가됨.")
    else:
        loc = rightAlphaLoc[i]
        rightTime = abs(loc[0] - srLoc[0]) + abs(loc[1] - srLoc[1])
        srLoc = loc
        totalTime += rightTime
        #print(f"{i} 누르러 오른쪽이 감: {rightTime}추가됨.")

print(totalTime + len(results))
