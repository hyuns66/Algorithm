# 회문

import sys

T = int(sys.stdin.readline())

answerList = []

for i in range(0, T):
    string = sys.stdin.readline().strip()
    start = 0
    end = len(string) - 1

    flag = 2
    chance = 1
    while True:
        if (start == end) | (end < start):  # 두 포인터가 중간에서 만나거나, 역전되면 끝
            flag = 0
            break

        if string[start] == string[end]:
            start += 1
            end -= 1
        else:  # 같지 않을 때는 유사 회문인지 검사

            startTemp = start
            endTemp = end

            if string[startTemp + 1] == string[endTemp]:  # 왼쪽 한 칸 땡기기
                startTemp += 1
                while True:
                    if (startTemp == endTemp) | (endTemp < startTemp):  # 두 포인터가 중간에서 만나거나, 역전되면 끝
                        flag = 1  # 유사회문
                        break

                    if string[startTemp] == string[endTemp]:
                        startTemp += 1
                        endTemp -= 1
                    else:
                        break

            startTemp = start
            endTemp = end

            if string[startTemp] == string[endTemp - 1]:  # 오른쪽 한 칸 땡기기
                endTemp -= 1
                while True:
                    if (startTemp == endTemp) | (endTemp < startTemp):  # 두 포인터가 중간에서 만나거나, 역전되면 끝
                        flag = 1  # 유사회문
                        break

                    if string[startTemp] == string[endTemp]:
                        startTemp += 1
                        endTemp -= 1
                    else:
                        break
            break  # 젤 바깥쪽 while True 문 탈출

    answerList.append(flag)

for i in range(0, T):
    print(answerList[i])

"""
시간초과:
리스트의 slicing은 잘라내는 부분의 원소를 전부 복사해서 새로운 리스트를 만드는 기능입니다. 
길이가 n인 리스트를 n번 자르는 데에는 O(n^2)의 시간이 소요됩니다.

유사회문 판별에는 N*N보다 적게 확인할 수있는 방법이 있습니다.
=> 투 포인터 이용하기
"""

"""
왜 틀렸지?
왼쪽 한칸 땡겨서 끝까지 되는지 해보고,
오른쪽 한칸 땡겨서 끝까지 되는지 둘다 해봐야하는데
왼쪽 한칸 땡겨서 그 단어끼리 맞으면 왼쪽만 하고 말았었다. 그게 문제.
"""
