import sys
from collections import deque

def make_temp():
    global sequence, temp
    while sequence:
        s = sequence.popleft()
        temp *= 10
        temp += int(s)
        if len(sequence) == 0 or sequence[0] == '-' or sequence[0] == '+':
            return


sequence = deque(list(sys.stdin.readline().rstrip()))
temp = 0
make_temp()
flag = False
answer = temp
temp = 0
while sequence:
    s = sequence.popleft()
    if s == '+':
        if flag:
            make_temp()
            answer -= temp
            temp = 0
        else:
            make_temp()
            answer += temp
            temp = 0
    elif s == '-':
        make_temp()
        answer -= temp
        temp = 0
        flag = True

print(answer)