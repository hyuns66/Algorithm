# A와 B 2 - unsolved
import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

possible = []

only = ''
for i in range(len(T)):
    if T[0] == 'A':
        if T[i] == 'B':
            only = T[:i+1]
    else:
        if T[i] == 'B':
            reversed_string = ''.join(reversed(T[i+1:]))
            possible.append(reversed_string)

possible.append(only)

#print(possible)

if S in possible:
    print(1)
else:
    print(0)

