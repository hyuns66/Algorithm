import sys

T = int(sys.stdin.readline())
test_case = [dict() for _ in range(T)]

for i in range(T):
    num = int(sys.stdin.readline())
    for j in range(num):
        cloth, category = sys.stdin.readline().split()
        if category not in test_case[i]:
            test_case[i][category] = [cloth]
        else:
            test_case[i][category].append(cloth)

for tc in test_case:
    answer = 1
    for key in tc.keys():
        answer *= len(tc[key]) + 1
    print(answer - 1)