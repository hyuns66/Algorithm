# 피카츄

import sys

S = sys.stdin.readline().strip()

i = 0
while True:
    if i > len(S)-1:
        break
    if i+2 <= len(S) and S[i] == 'p' and S[i + 1] == 'i':
        i += 2
    elif i+2 <= len(S) and S[i] == 'k' and S[i + 1] == 'a':
        i += 2
    elif i+3 <= len(S) and S[i] == 'c' and S[i + 1] == 'h' and S[i + 2] == 'u':
        i += 3
    else:
        break

if i > len(S)-1:
    print("YES")
else:
    print("NO")
