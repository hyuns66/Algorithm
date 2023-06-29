# 사탕

import sys

T = int(sys.stdin.readline())
answer = []
for i in range(0, T):
    J, N = map(int, sys.stdin.readline().split())
    box = []

    for i in range(0, N):
        Ri, Ci = map(int, sys.stdin.readline().split())
        box.append(Ri * Ci)

    box.sort(reverse=True)

    count = 1
    for i in range(0, len(box)):
        if J - box[i] <= 0:
            break
        count += 1
        J = J - box[i]
    answer.append(count)

for i in answer:
    print(i)

# sort는 리스트를 정렬하고, 정렬된 리스트를 반환하지 않는다.