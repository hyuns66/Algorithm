# 팰린드롬수

import sys
import math

answer = []
while True:
    line = sys.stdin.readline().strip()
    if line == '0':
        break
    flag = 1
    for i in range(math.floor(len(line)/2)):
        if (line[i]!=line[len(line)-1-i]):
            flag = 0
            break
    if flag:
        answer.append("yes")
    else:
        answer.append("no")

for i in answer:
    print(i)
