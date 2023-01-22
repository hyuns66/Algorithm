# 후위 표기식2

import sys

N = int(sys.stdin.readline())

mInput = sys.stdin.readline().strip()
mValue = []
for i in range(N):
    mValue.append(int(sys.stdin.readline()))

stack = []
for i in mInput:
    if i in "*+-/":
        Y = stack.pop()
        X = stack.pop()
        if i == "*":
            stack.append(X * Y)
        elif i == "/":
            stack.append(X / Y)
        elif i == "+":
            stack.append(X + Y)
        if i == "-":
            stack.append(X - Y)
    else:
        stack.append(mValue[ord(i) - ord('A')])

print(f'{stack.pop():0.2f}')

"""
후위표기식 계산하는 법:
피연산자면 순서대로 stack에 저장하다가,
연산자를 만나면 top에서 2개의 피연산자를 차례로 빼서 연산을 수행한다.
연산결과를 다시 stack에 넣어주고 반복한다!
"""