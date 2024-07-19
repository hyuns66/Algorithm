from math import sqrt

T = int(input())
for t in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if r1==r2 and x1==x2 and y1==y2:
        print(-1)
    elif r1+r2 == sqrt((x1-x2)**2 + (y1-y2)**2) or abs(r1-r2) == sqrt((x1-x2)**2 + (y1-y2)**2):     # 외접, 내접
        print(1)
    elif r1+r2 < sqrt((x1-x2)**2 + (y1-y2)**2) or abs(r1-r2) > sqrt((x1-x2)**2 + (y1-y2)**2):   # 내부, 외부 인접 x
        print(0)
    else:
        print(2)