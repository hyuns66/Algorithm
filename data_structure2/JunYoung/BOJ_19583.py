# 싸이버 개강총회
# 출석을 인정 받으려면, 개강총회 시작하기전에 입장 확인이 되어야하고
# 개강 총회 끝 ~ 개강총회 스트리밍 끝에 퇴장 확인이 되어야한다.

import sys

f = open("BOJ_19583_input.txt", 'r')
lines = f.readlines()

S, E, Q = map(str, lines[0].split())
chattingRecord = dict()

S_hour, S_minute = map(int, S.split(":"))
S = S_hour * 60 + S_minute

E_hour, E_minute = map(int, E.split(":"))
E = E_hour * 60 + E_minute

Q_hour, Q_minute = map(int, Q.split(":"))
Q = Q_hour * 60 + Q_minute

for chat in lines[1:]:
    time, name = map(str, chat.split())
    if name in chattingRecord:
        chattingRecord[name] = chattingRecord[name]+[time]
        # 왜 chattingRecord[name].append(time)은 안돼?
    else:
        chattingRecord[name] = [time]

answerCount = 0
for people in chattingRecord.keys():
    enterFlag = False
    exitFlag = False

    for time in chattingRecord[people]:
        hour, minute = map(int, time.split(":"))
        if (hour * 60 + minute) <= S:
            enterFlag = True
        if E <= (hour * 60 + minute) <= Q:
            exitFlag = True
    if enterFlag and exitFlag:
        answerCount += 1

print(answerCount)
f.close()

# 파이썬은 string이 아니라, str이다.
# 파이썬에서는 E <= (hour * 60 + minute) <= Q이 가능하다.
# &는 비트연산자, and는 논리연산자
# 딕셔너리 밸류에 리스트로 저장하는 법
