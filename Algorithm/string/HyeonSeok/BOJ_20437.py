import sys

T = int(sys.stdin.readline())
answer = list()
for _ in range(T):
    s = dict()
    W = list(sys.stdin.readline().rstrip())
    K = int(sys.stdin.readline())
    small = sys.maxsize
    big = -1
    for i in range(len(W)):
        if W[i] in s:
            s[W[i]].append(i)
        else:
            s[W[i]] = [i]
    for char in s:
        if len(s[char]) >= K:
            for i in range(len(s[char]) - K + 1):
                length = s[char][i + K - 1] - s[char][i] + 1
                if length < small:
                    small = length
                if length > big:
                    big = length
    if big == -1:
        answer.append(-1)
    else:
        answer.append((small, big))

for a in answer:
    if a != -1:
        print(a[0], a[1])
        continue
    print(a)
