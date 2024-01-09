# 그룹 단어 체커

import sys

N = int(sys.stdin.readline())

wordList = []
for i in range(0, N):
    wordList.append(sys.stdin.readline().strip())

groupWord = N
for i in wordList:
    alphabet = []
    for j in range(0, len(i)):
        if i[j] not in alphabet:
            alphabet.append(i[j])
        else:  # 같은 알파벳이 또 나오면 그룹단어가 아니다.
            if alphabet[-1] != i[j] :
                groupWord -= 1
                break

print(groupWord)
