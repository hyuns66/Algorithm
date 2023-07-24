# 톱니바퀴

import sys
from collections import deque

# N극은 0, S극은 1
wheel1 = deque(int(digit) for digit in sys.stdin.readline().strip())
wheel2 = deque(int(digit) for digit in sys.stdin.readline().strip())
wheel3 = deque(int(digit) for digit in sys.stdin.readline().strip())
wheel4 = deque(int(digit) for digit in sys.stdin.readline().strip())
K = int(sys.stdin.readline())  # 회전횟수

for i in range(K):
    state = []
    wheelNum, direction = map(int, sys.stdin.readline().split())
    if wheel1[2] == wheel2[-2]:
        state.append(0)
    else:
        state.append(1)

    if wheel2[2] == wheel3[-2]:
        state.append(0)
    else:
        state.append(1)

    if wheel3[2] == wheel4[-2]:
        state.append(0)
    else:
        state.append(1)

    if wheelNum == 1:
        if direction == -1:
            wheel1.rotate(-1)
        else:
            wheel1.rotate(1)

        if state[0] == 1:  # wheel2가 다른극이었으면
            if direction == -1:
                wheel2.rotate(1)
            else:
                wheel2.rotate(-1)

            if state[1] == 1:  # wheel3이 다른극이었으면
                if direction == -1:
                    wheel3.rotate(-1)
                else:
                    wheel3.rotate(1)

                if state[2] == 1:  # wheel4이 다른극이었으면
                    if direction == -1:
                        wheel4.rotate(1)
                    else:
                        wheel4.rotate(-1)
    elif wheelNum == 2:
        if direction == -1:
            wheel2.rotate(-1)
        else:
            wheel2.rotate(1)

        if state[0] == 1:  # wheel1이 다른극이었으면
            if direction == -1:
                wheel1.rotate(1)
            else:
                wheel1.rotate(-1)

        if state[1] == 1:  # wheel3이 다른극이었으면
            if direction == -1:
                wheel3.rotate(1)
            else:
                wheel3.rotate(-1)
            if state[2] == 1:  # wheel4이 다른극이었으면
                if direction == -1:
                    wheel4.rotate(-1)
                else:
                    wheel4.rotate(1)

    elif wheelNum == 3:
        if direction == -1:
            wheel3.rotate(-1)
        else:
            wheel3.rotate(1)

        if state[2] == 1:  # wheel4이 다른극이었으면
            if direction == -1:
                wheel4.rotate(1)
            else:
                wheel4.rotate(-1)

        if state[1] == 1:  # wheel2이 다른극이었으면
            if direction == -1:
                wheel2.rotate(1)
            else:
                wheel2.rotate(-1)
            if state[0] == 1:  # wheel1이 다른극이었으면
                if direction == -1:
                    wheel1.rotate(-1)
                else:
                    wheel1.rotate(1)

    if wheelNum == 4:
        if direction == -1:
            wheel4.rotate(-1)
        else:
            wheel4.rotate(1)

        if state[2] == 1:  # wheel3가 다른극이었으면
            if direction == -1:
                wheel3.rotate(1)
            else:
                wheel3.rotate(-1)

            if state[1] == 1:  # wheel2이 다른극이었으면
                if direction == -1:
                    wheel2.rotate(-1)
                else:
                    wheel2.rotate(1)

                if state[0] == 1:  # wheel1이 다른극이었으면
                    if direction == -1:
                        wheel1.rotate(1)
                    else:
                        wheel1.rotate(-1)

# print(wheel1[0], wheel2[0], wheel3[0], wheel4[0])

score = 0
if wheel1[0] == 1:
    score += 1
if wheel2[0] == 1:
    score += 2
if wheel3[0] == 1:
    score += 4
if wheel4[0] == 1:
    score += 8

print(score)
