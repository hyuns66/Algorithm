# 부분 문자열
import sys

S = sys.stdin.readline().strip()
P = sys.stdin.readline().strip()


def makeTable(P):
    lp = len(P)
    Table = [0] * lp
    i = 0
    for j in range(1, lp):
        while i > 0 and P[i] != P[j]:
            i = Table[i - 1]
        if P[i] == P[j]:
            i += 1
            Table[j] = i
    return Table


def KMP(P, T):
    result = []
    lp = len(P)
    table = makeTable(P)
    i = 0
    for j in range(len(T)):
        while i > 0 and P[i] != T[j]:
            i = table[i - 1]
        if P[i] == T[j]:
            i += 1
            if i == len(P):
                result.append(j - i + 1) # j(패턴 끝자리)- 패턴길이 +1까지 해줘야 찾은 패턴의 시작인덱스가 구해진다.
                i = table[i - 1]
    return result


answer = KMP(P, S)
if len(answer) != 0:
    print(1)
else:
    print(0)

"""
# 1차 시도
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
"""

"""
kmp알고리즘
https://chanhuiseok.github.io/posts/algo-14/
https://velog.io/@mein-figur/PythonKMP-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98
https://yiyj1030.tistory.com/495
"""
