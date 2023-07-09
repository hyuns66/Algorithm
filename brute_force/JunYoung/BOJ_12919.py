# A와 B 2 - unsolved
import sys


def back(str, targetLen):
    global possible
    possible.append(str)
    #print(possible)

    if len(str) == 1 or len(str) <= targetLen:  # 더 이상 되감기 할 필요가 없으므로
        return # 이걸 exit으로 하면 프로그램이 그냥 종료되어 버린다.
    if str[-1] == 'A':
        back(str[:-1], targetLen)
    if str[0] == 'B':
        reversedS = ''.join(reversed(str[1:]))
        back(reversedS, targetLen)


S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
targetLen = len(S)

possible = []
back(T, targetLen)

if S in possible:
    print(1)
else:
    print(0)

# 알고리즘 분류 중 재귀를 보고 풀었더니 쉽게 풀 수 있었다. (재귀를 통한 브루트포스)
