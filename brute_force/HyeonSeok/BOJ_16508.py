import sys
import copy

# 3 -> [0,1,1]  6 -> [1,1,0] 형태의 bit mask로 변환해주는 함수
def int_to_padded_binary_list(num, padding):
    binary_str = map(int, bin(num)[2:])  # 정수를 이진수 문자열로 변환하고 '0b' 접두사 제거
    binary_list = list(binary_str)  # 이진수 문자열을 정수 리스트로 변환

    # 패딩을 적용하여 비트 리스트 생성
    if len(binary_list) < padding:
        binary_list = [0] * (padding - len(binary_list)) + binary_list

    return binary_list


word = list(sys.stdin.readline().strip())
word_set = dict()   # 단어 구성에 필요한 글자 수 저장
N = int(sys.stdin.readline())
books = list()  # [가격, 제목] 형태의 리스트
word_dict = [dict() for j in range(N)]  # books에 있는 책 하나당 단어구성에 필요한 글자를 얼마나 가지고 있는지 저장

# 가지고 있는 책들을 초기화
for i in range(N):
    price, title = sys.stdin.readline().rstrip().split()
    price = int(price)
    title = list(title)
    books.append([price, title])

# 만들 단어를 글자별로 쪼개서 등장한 횟수를 dictionary로 구성
for ch in word:
    if ch not in word_set:
        word_set[ch] = 1
    else:
        word_set[ch] += 1

# print(word_dict)
# print(word_set)

# 가지고 있는 책들에서 단어를 만들 수 있는 글자가 얼마나 등장하는지 dictionary로 각각 구성
for idx, book in enumerate(books):
    price, title = book
    bit_mask = []
    for char in title:
        if char in word_set:
            if char not in word_dict[idx]:
                word_dict[idx][char] = 1
            else:
                word_dict[idx][char] += 1
# print(word_dict)

# 비트마스크 조합 풀이
answer = sys.maxsize
for combination in range(1, 2**N):
    comb_mask = int_to_padded_binary_list(combination, N)
    dict_cnt = copy.deepcopy(word_set)
    cost = 0
    # print(comb_mask)
    for i in range(N):
        if comb_mask[i] == 1:
            cost += books[i][0]
            for idx, value in word_dict[i].items():
                if dict_cnt[idx] > 0:
                    dict_cnt[idx] = max(0, dict_cnt[idx]-value)
    # print(cost)
    if all(value == 0 for value in dict_cnt.values()):
        answer = min(answer, cost)

print(answer if answer != sys.maxsize else -1)