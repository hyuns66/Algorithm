import sys

N = int(input())
VPSlist = list()

# 1. 시작을 )로 한 경우
# 2. 끝까지 다 돌았는데 괄호가 다 안닫힌 경우
def vpscheck(string):
    VPScnt = 0
    strlist = list(string)
    for i in range(len(strlist)):
        if strlist[i] == '(':
            VPScnt += 1
        elif strlist[i] == ')':
            VPScnt -= 1
            if VPScnt < 0:
                return "NO"    # 1번 케이스
    if VPScnt == 0:
        return "YES"
    else:
        return "NO"    # 2번 케이스


for i in range(N):
    string = sys.stdin.readline()
    VPSlist.append(vpscheck(string))

for i in range(N):
    print(VPSlist[i])