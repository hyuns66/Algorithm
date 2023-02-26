import sys

N = int(sys.stdin.readline().rstrip())
muscle_loss = list(map(int, sys.stdin.readline().split()))
muscle_loss.sort()

answer = 0
if (1 & N) == 1:
    answer = muscle_loss.pop()
    N -= 1
temp = 0
for i in range(N//2):
    temp += muscle_loss[i]
    temp += muscle_loss[N-1-i]
    answer = max(answer, temp)
    temp = 0

print(answer)