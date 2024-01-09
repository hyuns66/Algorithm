# 좋은 단어

import sys

N = int(sys.stdin.readline())

words = []
for i in range(N):
    words.append(sys.stdin.readline().strip())

goodWords = 0

for w in words:
    S = []
    for s in w:
        if len(S) != 0 and S[-1] == s:
            S.pop()
        else:
            S.append(s)
    if len(S) == 0:
        goodWords += 1

print(goodWords)
