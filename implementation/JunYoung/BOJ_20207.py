# 달력

import sys

N = int(sys.stdin.readline())

calendar = {}  # key는 날짜, value는 일정 개수
for _ in range(N):
    S, E = map(int, sys.stdin.readline().split())
    for day in range(S, E + 1):  # 시작~ 종료 날짜까지
        if day in calendar:
            calendar[day] += 1
        else:
            calendar[day] = 1

days = sorted(calendar.keys())
startDay = days[0]
endDay = days[-1]

totalSize = 0
maxSchedule = 0
tempStart = startDay

for i in range(startDay, endDay+2):
    if i in calendar:
        if calendar[i]>maxSchedule:
            maxSchedule = calendar[i]
    else:
        totalSize += maxSchedule*(i-tempStart) #이때 i는 젤 마지막 연속된 일정 하루 뒤
        #print(str(maxSchedule*(i-tempStart))+"추가됨")
        maxSchedule = 0
        tempStart = i+1

print(totalSize) 

# (일정이 이어지는 날짜 수 * 그 기간동안의 maximumSchedule) = 코팅지 크기