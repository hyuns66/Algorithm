import sys
import copy

def step(sequence):
    global S, answer
    if sequence == S:
        answer = 1
        print(answer)
        sys.exit(0)
    if len(sequence) <= len(S):
        return
    a_seq = copy.deepcopy(sequence[:-1])
    b_seq = copy.deepcopy(sequence[::-1][:-1])
    if sequence[0] == 'A' and sequence[-1] == 'B':
        return
    if sequence[0] == 'A' and sequence[-1] == 'A':
        step(a_seq)
    if sequence[0] == 'B' and sequence[-1] == 'B':
        step(b_seq)
    if sequence[0] == 'B' and sequence[-1] == 'A':
        step(a_seq)
        step(b_seq)

S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()

answer = 0
step(T)
print(answer)
