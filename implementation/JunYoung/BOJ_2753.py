# 윤년

import sys

year = int(sys.stdin.readline().strip())

yoonYear = False
if year % 400 == 0:
    yoonYear = True
elif year % 4 == 0 and year % 100 != 0:
    yoonYear = True

if yoonYear:
    print(1)
else:
    print(0)
