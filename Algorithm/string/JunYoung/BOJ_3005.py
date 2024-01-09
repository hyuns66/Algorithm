# 크로스워드 퍼즐 쳐다보기

import sys

R, C = map(int, sys.stdin.readline().split())

cross = [list(sys.stdin.readline().strip()) for i in range(R)]

#print(cross)

words = set()

for i in range(R):
    temp = []
    for j in range(C):
        if cross[i][j] == '#':
            if len(temp) >= 2:
                words.add("".join(temp))
            temp = []
        else:
            temp.append(cross[i][j])

    if len(temp) >= 2:
        words.add("".join(temp))

for j in range(C):
    temp = []
    for i in range(R):
        if cross[i][j] == '#':
            if len(temp) >=2:
                words.add("".join(temp))
            temp = []
        else:
            temp.append(cross[i][j])

    if len(temp) >= 2:
        words.add("".join(temp))

#print(words)
new_words = list(words)
new_words.sort()

print("".join(new_words[0]))
