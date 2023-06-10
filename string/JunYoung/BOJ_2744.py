# 대소문자 바꾸기

import sys
line = sys.stdin.readline().strip()

answer = []
for i in range(len(line)):
    if line[i].islower():
        answer.append(line[i].upper())
    else:
        answer.append(line[i].lower())

for i in answer:
    print(i, end='')
