import sys

def check(sequence):
    stack = list()
    stack.append(sequence[0])
    for i in range(1, len(sequence)):
        if not stack or stack[-1] != sequence[i]:
            stack.append(sequence[i])
        else:
            stack.pop()
    if stack:
        return 0
    else:
        return 1

answer = 0
N = int(sys.stdin.readline())
sequences = list()
for _ in range(N):
    seq = list(sys.stdin.readline().rstrip())
    answer += check(seq)
print(answer)