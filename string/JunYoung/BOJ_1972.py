# 놀라운 문자열
import sys

answer = []
while True:
    inp = sys.stdin.readline().strip()
    N = len(inp)
    if inp == "*":
        break
    else:
        surprising = True
        for d in range(0, N-2+1):
            ssang = []
            for j in range(N):
                if j+d+1 < N:
                    ssang.append(inp[j] + inp[j+d+1])
            if len(ssang) != len(set(ssang)):
                surprising = False
                break

        if surprising:
            answer.append(inp + " is surprising.")
        else:
            answer.append(inp + " is NOT surprising.")

for i in answer:
    print(i)
