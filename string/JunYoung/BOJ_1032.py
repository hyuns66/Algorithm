# 명령 프롬프트

import sys

N = int(sys.stdin.readline())

l1 = sys.stdin.readline().strip()
answer = list(0 for i in range(len(l1)))
for i in range(len(l1)):
    answer[i] = l1[i]

for i in range(N-1):
    tempSentence = sys.stdin.readline().strip()
    for j in range(len(tempSentence)):
        if tempSentence[j] != answer[j]:
            answer[j] = "?"

for i in answer:
    print(i, end = '')
