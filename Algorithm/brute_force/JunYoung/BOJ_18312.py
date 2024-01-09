# 시각

import sys

N, K = map(int, sys.stdin.readline().split())

N_sec = N*60*60 + 59*60 + 59

now = 0
count = 0
while now <= N_sec:
    hour = int(now/3600)
    min = int((now - hour*3600) /60)
    sec = now % 60

    shour = str(hour)
    smin = str(min)
    ssec = str(sec)
    if len(shour) == 1:
        shour = '0'+shour
    if len(smin) == 1:
        smin = '0' + smin
    if len(ssec) == 1:
        ssec = '0' + ssec

    time = shour + smin + ssec

    for i in time:
        if i == str(K):
            #print(time)
            count += 1
            break
    now += 1

print(count)

# 0도 채워줘야한다.
