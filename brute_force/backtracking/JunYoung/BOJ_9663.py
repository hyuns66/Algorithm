# N-Queen

import sys

N = int(sys.stdin.readline())


def backtracking(n, y, width, diagonal1, diagonal2):
    answer = 0
    if y == n:
        answer += 1
    else:
        for i in range(n):
            if width[i] or diagonal1[i + y] or diagonal2[(n - i) + y]:
                continue
            width[i] = diagonal1[i + y] = diagonal2[(n - i) + y] = True
            answer += backtracking(n, y + 1, width, diagonal1, diagonal2)
            width[i] = diagonal1[i + y] = diagonal2[(n - i) + y] = False
    return answer


solution = backtracking(N, 0, [False] * N, [False] * (2 * N), [False] * (2 * N))
print(solution)
