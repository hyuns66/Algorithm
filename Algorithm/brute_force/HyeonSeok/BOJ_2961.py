import sys

N = (int)(sys.stdin.readline())
ingredients = [[0 for i in range(2)] for j in range(N)]
flag = [[0 for i in range(N)] for j in range(2**N)]     # 나올 수 있는 모든 레시피의 경우의 수를 담고있는 배열
                                                        # N개의 재료에 대해 각 재료를 넣냐 안넣냐니까 2^N 개의 경우의 수를 담은 2차원 배열

for i in range(N):  # 재료 N개 입력받기
    ingredients[i][0], ingredients[i][1] = map(int, sys.stdin.readline().split())

for i in range(len(flag)):  # 2^N 개의 모든 경우의 수를 생성하는 반복문
    binary_flag = format(i, 'b').zfill(N)   # i 를 2진수로 깔끔하게 변환 ,   zfill : N 자리수 만큼 zero padding
    flag[i] = [int(a) for a in binary_flag]    # 2진수 binary_flag를 문자열로 변환 후 다시 int형 배열로 저장.
                                                    #  1011 -> [1, 0, 1, 1] -> 1, 3, 4번 재료를 사용한다는 의미

min = sys.maxsize
for i in range(1, len(flag)):   # 아무 재료도 넣지 않는 케이스가 0번 인덱스이므로 제외. 1번부터 시작
    S = 1   # 신맛은 곱이니까 1초기화
    B = 0   # 쓴맛은 합이니까 0초기화
    for j in range(N):
        if flag[i][j] == 1:         # flag가 1이면 사용한 재료로 간주, 신맛과 쓴맛 계산
            S *= ingredients[j][0]
            B += ingredients[j][1]
    temp = abs(S-B)         # 신맛과 쓴맛 차이 구해서 min과 비교, 최소값이면 업데이트
    if min > temp:
        min = temp

print(min)