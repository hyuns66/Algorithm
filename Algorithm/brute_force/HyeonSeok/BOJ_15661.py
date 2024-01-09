import sys

N = (int)(sys.stdin.readline())

stat = [[0 for i in range(N)] for j in range(N)]       # 스탯표 입력받기

for i in range(N):
    stat[i] = list(map(int,(sys.stdin.readline().split())))

team = [[0 for i in range(N)] for j in range(2**N-2)]
for i in range(1, 2**N-1):
    binary_flag = format(i, 'b').zfill(N)       # i 를 2진수로 깔끔하게 변환 ,   zfill : N 자리수 만큼 zero padding
    team[i-1] = [int(a) for a in binary_flag]     # 2진수 binary_flag를 문자열로 변환 후 다시 int형 배열로 저장.
                                                    #  1011 -> [1, 0, 1, 1] -> 1이면 link 팀 0이면 start 팀
result = sys.maxsize

for i in range(2**N-2):     # 모든 팀빌딩 경우의 수에 대해 탐색
    link_stat, start_stat = 0, 0
    link, start = set(), set()      # 한팀에 같은사람 중복되서 들어가지않게 집합으로 선언
    for j in range(N):
        if team[i][j] == 0:         # 0이면 start팀
            start.add(j)
        else:                       # 1이면 link 팀에 배정
            link.add(j)
    for i in link:                      # link팀의 사람들 스탯 다 더해서 합치기
        for j in link:
            link_stat += stat[i][j]
    for i in start:                     # start 팀도
        for j in start:
            start_stat += stat[i][j]
    if abs((link_stat - start_stat)) < result:          # 최소값 산출
        result = abs((link_stat - start_stat))

print(result)