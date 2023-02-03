import sys

T = int(sys.stdin.readline())
answer = list()
for _ in range(T):
    string = list(sys.stdin.readline().rstrip())
    start, end = 0, len(string)
    status = 0
    while start <= end:
        if string[start] == string[end - 1]:
            start += 1
            end -= 1
        else:
            if status == 0:
                status = 1
                if string[start] == string[end - 2]:
                    end -= 1
                elif string[start + 1] == string[end - 1]:
                    start += 1
            else:
                status = 2
                break
    answer.append(status)

print(*answer)
