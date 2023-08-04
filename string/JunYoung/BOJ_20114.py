# 미아 노트

import sys

N, H, W = map(int, sys.stdin.readline().split())

s = [set() for i in range(N)]

for i in range(H):
    line = sys.stdin.readline().strip()
    for j in range(len(line)):
        index = j//W
        s[index].add(line[j])

#for i in s:
#    print(i)

answers = []
for hint in s:
    answer = '?'
    for j in hint:
        if 'a' <= j <= 'z':
            answer = j
    answers.append(answer)

for i in answers:
    print(i, end='')


