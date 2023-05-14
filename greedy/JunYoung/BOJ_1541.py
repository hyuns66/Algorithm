# 잃어버린 괄호

import sys
from collections import deque

exp = sys.stdin.readline().strip()
newexp = ['0' for i in range(0, len(exp))]
flag = 0
for i in range(0, len(exp)):
    if flag == 0:
        if exp[i] == '-':
            flag = 1
        newexp[i] = exp[i]
    else:
        if exp[i] == '+':
            newexp[i] = '-'
        else:
            newexp[i] = exp[i]

#print(newexp)

num = deque()
math = deque()
temp = ''
for i in newexp:
    if i == '+' or i =='-':
        num.append(int(temp))
        math.append(i)
        temp = ''
    else:
        temp += i

num.append(int(temp))

#print(num)
#print(math)

for i in math:
    if i == '+':
        a = num.popleft()
        b = num.popleft()
        num.appendleft(a+b)
    else:
        a = num.popleft()
        b = num.popleft()
        num.appendleft(a - b)

print(num.pop())

# 'str' object does not support item assignment
# 문자열은 불변(immutable)한 객체로, 한 번 생성되면 수정할 수 없습니다.
