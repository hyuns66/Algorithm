# N과 M (5)
# N개의 자연수는 모두 다른 수이다.
# N개의 자연수 중에서 M개를 고른 수열

import sys

N, M = map(int, sys.stdin.readline().split())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

answers = []


def backtracking(selected_num, visited):
    #print(selected_num)
    #print(visited)
    if len(selected_num) == M:
        answers.append(selected_num)
        return

    for i in range(N):
        if N_list[i] in visited:
            continue
        else:
            # visited.add(N_list[i])
            backtracking(selected_num + [N_list[i]], visited|{N_list[i]})


backtracking([], set())

for a in answers:
    print(*a)

# visited.add(N_list[i])를 해서 visited를 매개변수로 넘겨주면 동일한 visited 객체가 공유된다.
# 반면, visited|{N_list[i]}를 사용하면 새로운 집합을 생성하여 이를 사용하게 된다
# 따라서 각 호출간에 독립적으로 작동한다.
# 이거 때문에 답이 제대로 안 나왔었다~!!
