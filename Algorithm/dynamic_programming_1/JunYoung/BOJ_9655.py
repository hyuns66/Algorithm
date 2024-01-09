# 돌 게임

import sys

N = int(sys.stdin.readline())

"""
if N % 2 == 0:
    print("CY")
else:
    print("SK")
"""

print("CY" if 1 & N == 0 else "SK")
"""
1 상근
2 창영
3 상근
4 창영
5 4,2 상근
6 5,3 창영
"""
