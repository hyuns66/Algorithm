# N과 M(4)
# M개를 고른 수열
# 같은 수를 여러 번 골라도 된다.
# 오름차순 수열

import sys

N, M = map(int, sys.stdin.readline().split())

answers = []


def backtracking(start, selected_num):
    if len(selected_num) == M:  # 이걸 만족하면 종료
        answers.append(selected_num)
        return

    for i in range(start, N+1):
        backtracking(i, selected_num + [i])


backtracking(1, [])

for i in answers:
    print(*i)

# AttributeError는 변수나 객체가 None일 때 해당 속성이나 메서드를 참조하려고 할 때 발생합니다.
# .add()처럼 반환값이 없는걸 매개변수로 넘기는 실수 주의하기!
