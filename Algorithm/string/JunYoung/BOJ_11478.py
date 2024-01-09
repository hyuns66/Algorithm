# 서로 다른 부분 문자열의 개수

import sys

S = sys.stdin.readline().strip()
substring = set()

l = 1
while True:
    if l > len(S):
        break

    for i in range(len(S)):
        if i+l <= len(S):
            substring.add(S[i:i+l])
    l += 1

print(len(substring))
