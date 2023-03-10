import sys

S = list(sys.stdin.readline().rstrip())
answer = ""
point = 0

while point < len(S):
    char = S[point]
    if char == '<':
        while S[point] != '>':
            answer += S[point]
            point += 1
        answer += S[point]
        point += 1
        continue
    elif char != ' ':
        temp = ''
        while point < len(S) and S[point] != ' ' and S[point] != '<':
            temp = S[point] + temp
            point += 1
        answer += temp
    else:
        answer += char
        point += 1

print(answer)