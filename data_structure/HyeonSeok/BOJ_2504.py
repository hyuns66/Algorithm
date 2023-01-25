import sys
from collections import deque

brackets = deque(list(sys.stdin.readline()))
brackets.pop()
answer = list()
temp = 1

stack = list()
stack.append(brackets.popleft())
while len(brackets) != 0:
    if brackets[0] == '(' or brackets[0] == '[':
        if len(stack) == 0:
            answer.append(temp)
            temp = 1
        else:

        stack.append(brackets.popleft())
    if brackets[0] == ')' or brackets[0] == ']':
        while brackets[0] != '(' and brackets[0] != '[':
            if brackets[0] == ')':
                if stack[-1] == '(':
                    temp *= 2
                    brackets.popleft()
                    stack.pop()
                else:
                    print(0)
                    sys.exit()
            elif brackets[0] == ']':
                if stack[-1] == '[':
                    temp *= 3
                    brackets.popleft()
                    stack.pop()
                else:
                    print(0)
                    sys.exit()
answer += temp

print(answer)
