import sys

def update_cnt(cnt, data_set):
    for d in data_set:
        if int(d) & 1 == 1:
            cnt += 1
    return cnt

def operate_num(cnt, *args):
    global a_max, a_min
    temp = 0
    c = cnt
    if len(args) == 1 and len(args[0]) == 1:
        a_max = max(a_max, c)
        a_min = min(a_min, c)
        return
    for a in args:
        num = int(''.join(a))
        temp += num
    temp_list = list(str(temp))
    c = update_cnt(c, temp_list)
    if len(temp_list) == 1:
        operate_num(c, temp_list[0])
    elif len(temp_list) == 2:
        operate_num(c, temp_list[0], temp_list[1])
    else:
        for i in range(1, len(temp_list)):
            for j in range(i+1, len(temp_list)):
                operate_num(c, temp_list[:i], temp_list[i:j], temp_list[j:])

N = list(sys.stdin.readline().rstrip())
cnt = 0
a_min = sys.maxsize
a_max = 0
operate_num(cnt, N)
print(a_min, a_max)
