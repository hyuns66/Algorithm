# 꽃길
 
import sys
import itertools

N = int(sys.stdin.readline())

garden = []
for i in range(N):
    garden.append(list(map(int, sys.stdin.readline().split())))

cost = []
choice = []
for i in range(1, N - 1):
    row = []
    for j in range(1, N - 1):
        choice.append([i, j])
        #print(f"i:{i}/ j:{j}")
        price = garden[i + 1][j] + garden[i - 1][j] + garden[i][j - 1] + garden[i][j + 1] + garden[i][j]
        row.append(price)
    cost.append(row)

plant = [[0 for i in range(N)] for j in range(N)]
# 테두리에 1 넣기 (1은 씨앗을 심을 수 없다.)
plant[0] = [1 for i in range(N)]
plant[N - 1] = [1 for i in range(N)]
for i in range(N):
    plant[i][0] = 1
    plant[i][N - 1] = 1

nC3 = itertools.combinations(choice, 3)

notOverlapSeedsCase = []

for seedsCase in nC3:
    check = [[0 for i in range(N)] for j in range(N)]
    flag = True
    #print(f"seedsCase-----{list(seedsCase)}")
    for s in list(seedsCase): #점3개에서 씨앗 하나씩 빼오기
        #print(f"s-------{s}")
        #print("check-----")
        #for i in check:
        #    print(i)
        #print(f"{s[0]},{s[1]}")
        #print(f"상:{check[s[0]-1][s[1]]}/하:{check[s[0]+1][s[1]]}/좌:{check[s[0]][s[1] - 1]}/우:{check[s[0]][s[1] + 1]}")
        if check[s[0] + 1][s[1]] == 0 and check[s[0]-1][s[1]] == 0 and check[s[0]][s[1] - 1]==0 and check[s[0]][s[1] + 1]==0:
            #print(f"{s[0]},{s[1]} 위치에 심기 성공")
            check[s[0]][s[1]], check[s[0] - 1][s[1]], check[s[0] + 1][s[1]], check[s[0]][s[1] - 1], check[s[0]][s[1] + 1] = 1, 1, 1, 1, 1
        else:
            #print(f"{s[0]},{s[1]} 위치에 심기 실패")
            flag = False
            break
    if flag:
        notOverlapSeedsCase.append(seedsCase)
        #print(f"성공적인 seedsCase:{seedsCase}")


casePrice = {}
#print(f"notOverlapSeedsCase:{notOverlapSeedsCase}")
caseNum = 0
for case in notOverlapSeedsCase:
    #print(f"case:{case}")
    totalPrice = 0
    for index in range(len(case)):
        c = cost[case[index][0]-1][case[index][1]-1]
        totalPrice += c
        #print(f"index:{index}번째 씨앗, 가격:{c}")
    casePrice[caseNum] = totalPrice
    #print(f"casePrice:{casePrice}")
    caseNum += 1

#print(f"casePrice:{casePrice}")
results = sorted(casePrice.items(), key=lambda x: x[1])

#print(f"results:{results}")
print(results[0][1])

# combination 함수 - import itertools
# https://velog.io/@dramatic/Python-permutation-combination-%EC%88%9C%EC%97%B4%EA%B3%BC-%EC%A1%B0%ED%95%A9

# 딕셔너리 정렬

# 좀 과하게 코딩됐지만... 뭐..