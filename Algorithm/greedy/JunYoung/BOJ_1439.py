# 뒤집기

import sys

S = sys.stdin.readline().strip()

sdict = {}
sdict['0'] = 0
sdict['1'] = 0
## 딕셔너리에 키로 들어갈 때 0과 '0'은 다른 것이다! => 키라고 다 숫자형으로 들어가는 게 아니다.

# 마지막에 있는 것도 체크해주기 위해서
if S[-1] == '0':
    S = S + '1'
else:
    S = S + '0'
#print(S)
prev = S[0]
for i in range(1, len(S)):
    if S[i] == '0':
        if S[i] != prev:
            sdict[prev] += 1
    else:
        if S[i] != prev:
            sdict[prev] += 1

sorted_list = sorted(sdict.keys(), key=lambda x: sdict[x], reverse=True)
#print(sorted_list)
needChange = sorted_list[-1]

count = 0
flag = 0
for i in range(len(S)):
    if S[i] == str(needChange):
        if flag == 0:
            flag = 1
    else:
        if flag == 1:
            flag = 0
            count += 1

print(count)
