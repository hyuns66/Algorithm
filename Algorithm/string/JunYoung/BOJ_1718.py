#암호

import sys
import string
m = sys.stdin.readline().strip()
key = sys.stdin.readline().strip()

newKey = []
for i in range(len(m)):
    index = i%len(key)
    newKey.append(key[index])

nK = ''.join(newKey)
alpha = list(string.ascii_lowercase)

alphaDict = {}
for i in range(len(alpha)):
    alphaDict[alpha[i]] = 1+i

answer = []
for i in range(len(m)):
    if m[i] == ' ':
        answer.append(' ')
        continue
    a = alphaDict[m[i]]
    b= alphaDict[nK[i]]
    c = a-b
    if a-b <= 0:
        c = a-b+26
    result = chr(ord('a') + c-1)
    answer.append(result)

for i in answer:
    print(i, end='')