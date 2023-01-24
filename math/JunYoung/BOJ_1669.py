# 멍멍이 쓰다듬기

import sys

X, Y = map(int, sys.stdin.readline().split())

countDay = 0
total = 0
index = 0
for i in range(1, (Y - X) + 1):
    total += i
    if (2 * total) > (Y - X):
        index = i - 1
        break

countDay = 2 * index
#print(index)
#print(total-index+1)
ing = 0
for i in range(1, index+1):
    ing += i

if Y-X == 0:
    countDay = 0
elif Y - X - (2 * ing) in (index - 1, index, index + 1):
    countDay += 1
elif Y - X - (2 * ing) != 0:
    countDay += 2

print(countDay)

"""
// 1번
input:
41707 2147483647
    
correct answer:
92680
    
// 2번
input:
0 1523990
    
correct answer:
2468
"""