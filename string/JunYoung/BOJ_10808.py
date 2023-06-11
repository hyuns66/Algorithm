# 알파벳 개수

import sys
import string

S = sys.stdin.readline().strip()

alpha = string.ascii_lowercase.strip()
alphaDict = {}

#print(alpha)
for i in alpha:
    alphaDict[i] = 0
# 초기화 완료

for i in range(len(S)):
    alphaDict[S[i]] = alphaDict[S[i]] + 1

for i in alphaDict.values():
    print(i, end = ' ')
