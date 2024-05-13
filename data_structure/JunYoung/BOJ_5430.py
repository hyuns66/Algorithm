# AC
# R = 뒤집기
# D = 버리기
# [TIP] = 뒤집는다고 해서 진짜 뒤집을 필요는 없음! 우리는 앞에서 뺄지, 뒤에서 뺄지만 알면 되고, 나중에 결과물을 출력할 때만 뒤집힌거 반영해서 해주면 된다.

import sys
from collections import deque


def make_list_str(list, reverse):
    if len(list) == 0:
        return "[]"

    val = "["
    if reverse:
        for i in range(len(list)):
            val += str(list[-i - 1]) + ","
    else:
        for i in range(len(list)):
            val += str(list[i]) + ","

    return val[:-1] + "]"


T = int(sys.stdin.readline())
answers = []
for i in range(T):
    command = sys.stdin.readline().strip()
    n = int(sys.stdin.readline())

    # 배열로 받기
    array_str = sys.stdin.readline().strip()
    array = []
    if array_str != "[]":
        array = deque(list(map(int, array_str[1:-1].split(","))))
    # print(array)

    flag = True
    error = False
    for c in command:
        if c == "R":
            flag = not flag
        elif c == "D":
            if len(array) == 0:
                error = True
                break
            if flag:
                array.popleft()
            else:
                array.pop()
    if error:
        answers.append("error")
    else:
        answer = make_list_str(list(array), not flag)
        answers.append(answer)

for a in answers:
    print(a)
