# 경고

import sys

nowTime = list(map(int, sys.stdin.readline().split(":")))
planTime = list(map(int, sys.stdin.readline().split(":")))

nowTimeSec = nowTime[0]*60*60+nowTime[1]*60+nowTime[2]
planTimeSec = planTime[0]*60*60+planTime[1]*60+planTime[2]

totalSec = 0
if nowTimeSec > planTimeSec:
    totalSec = 24*60*60-nowTimeSec+planTimeSec
else:
    totalSec = planTimeSec-nowTimeSec

if totalSec == 0:
    print("24:00:00")  # 적어도 1초 이상 기다려야하므로
else:
    leftSec = totalSec % 60
    leftMin = int(totalSec / 60)
    leftHour = int(leftMin / 60)
    leftMin = leftMin - leftHour * 60

    print(str(leftHour).zfill(2) + ":" + str(leftMin).zfill(2) + ":" + str(leftSec).zfill(2))

"""
zfill = 문자열 타입에서 원하는 총 자릿수를 지정, 빈 공간에 0을 채워줄 수 있다.
"""

"""
틀린 예시
00:00:00
00:00:00
정답: 24:00:00인데, 00:00:00을 출력했었다.
"""