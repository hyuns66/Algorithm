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
                t_start = start + 1
                t_end = end
                while t_start <= t_end:
                    if string[t_start] == string[t_end - 1]:
                        t_start += 1
                        t_end -= 1
                    else:
                        status = 0
                        break
                if status == 1:
                    break
                status = 1
                t_start = start
                t_end = end - 1
                while t_start <= t_end:
                    if string[t_start] == string[t_end - 1]:
                        t_start += 1
                        t_end -= 1
                    else:
                        status = 2
                        break
        if status != 0:
            break
    answer.append(status)

for a in answer:
    print(a)
