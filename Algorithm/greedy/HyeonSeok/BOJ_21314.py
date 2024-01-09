import sys
from collections import deque


def make_small(data):
    global small
    while data:
        s = data.popleft()
        if s == 'M':
            temp = 0
            while data[0] == 'M':
                data.popleft()
                temp += 1
            num = 10 ** temp
            small += str(num)
        elif s == 'K':
            small += '5'

def make_big(data):
    global big
    while data:
        s = data.popleft()
        if s == 'M':
            temp = 1
            flag = True
            while data:
                s_t = data.popleft()
                if s_t == 'M':
                    temp += 1
                elif s_t == 'K':
                    num = 5 * (10 ** temp)
                    big += str(num)
                    flag = False
                    break
            if flag:
                for _ in range(temp):
                    big += '1'
        elif s == 'K':
            big += '5'


sequence = list(sys.stdin.readline())

small = ''
big = ''

make_small(deque(sequence[:]))
make_big(deque(sequence[:]))
print(big)
print(small)
