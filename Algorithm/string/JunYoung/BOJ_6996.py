# 애너그램
import sys
from collections import deque

T = int(sys.stdin.readline())

answer = []
for i in range(T):
    flag = 1
    A, B = map(str, sys.stdin.readline().strip().split())
    alpha = deque()
    for i in A:
        alpha.append(i)

    for j in B:
        try:
            alpha.remove(j)
        except ValueError:
            flag = 0
            break

    if len(alpha) != 0:
        flag = 0

    if flag:
        answer.append(A+" & "+B+" are anagrams.")
    else:
        answer.append(A + " & " + B + " are NOT anagrams.")

for i in answer:
    print(i)
