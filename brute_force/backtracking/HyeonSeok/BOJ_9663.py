"""
퀸은 각 열과 행에 하나씩만 존재
대각선체크만 잘 해서 시간복잡도 효율적으로 설계
"""

import sys

def canNotBeAttacked(y, x, queens):
    for queen in queens:
        queen_y, queen_x = queen
        if abs(queen_y - y) == abs(queen_x - x):
            return False
    return True

def backTracking(depth, cols, queens : set):
    global N, answer
    if depth == N:
        answer += 1
        return
    for i in range(N):
        if not cols[i] and canNotBeAttacked(depth, i, queens):
            cols[i] = True
            queens.add((depth, i))
            backTracking(depth+1, cols, queens)
            queens.remove((depth, i))
            cols[i] = False
    
                
N = int(sys.stdin.readline())
answer = 0
cols = [False for _ in range(N)]
backTracking(0, cols, set())
print(answer)