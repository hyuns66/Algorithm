# 부분 문자열
import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()

flag = False
for i in range(0, len(S)):
    if len(S) - i < len(P):  # 맞출 애보다 남은게 적으면
        break

    if S[i] == P[0]:
        for j in range(0, len(P)):
            if ((i + j) < len(S)) and (S[i + j] == P[j]):
                flag = True
            else:
                flag = False
                break

    if flag:
        break

if flag:
    print(1)
else:
    print(0)
