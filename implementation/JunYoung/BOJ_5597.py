# 과제 안 내신 분..?

import sys

students = [0 for i in range(30)]
for i in range(28):
    s = int(sys.stdin.readline()) -1
    students[s] = 1

answer = []
for i in range(len(students)):
    if students[i] == 0:
        answer.append(i+1)
        if len(answer)==2:
            break

for i in answer:
    print(i)
