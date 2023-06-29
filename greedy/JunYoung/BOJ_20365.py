# 블로그2

import sys

N = int(sys.stdin.readline())
blog = sys.stdin.readline().strip()

prev = '0'
blueBlock = 0
redBlock = 0
for i in range(0, len(blog)):
    if i == 0:
        prev = blog[i]
    else:
        if prev == 'B':
            if blog[i] == 'R':
                blueBlock += 1
        else:  # R일때
            if blog[i] == 'B':
                redBlock += 1
        prev = blog[i]

        if i == len(blog) - 1:
            if blog[i] == 'R':
                redBlock += 1
            else:
                blueBlock += 1

print(min(redBlock, blueBlock) + 1)
