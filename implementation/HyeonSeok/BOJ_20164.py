from collections import deque
import sys

def split_N(N : list):
    size = len(N)
    result = list()
    if size == 1:
        return [[N[0]]]
    if size == 2:
        return [[[N[0]], [N[1]]]]
    for i in range(1, size):
        for j in range(i+1, size):
            result.append([N[:i], N[i:j], N[j:]])
    return result

def make_number(num_list):
    size = len(num_list) - 1
    result = 0
    for n in num_list:
        n = int(n)
        n *= 10 ** size
        result += n
        size -= 1
    return result

def calc_sum(split_nums):
    result = 0
    for nums in split_nums:
        num = make_number(nums)
        result += num
    return result

def number_to_list(num):
    result_list = [int(digit) for digit in str(num)]
    return result_list

def count_odds(numbers):
    result = 0
    for n in numbers:
        if int(n) & 1:
            result += 1
    return result

def back_tracking(number_list, answer):
    global answer_min, answer_max
    answer += count_odds(number_list)
    if len(number_list) == 1:
        answer_min = min(answer_min, answer)
        answer_max = max(answer_max, answer)
        return
    split_numbers = split_N(number_list)
    for splits in split_numbers:
        new_number = 0
        for split in splits:
            new_number += make_number(split)
        back_tracking(number_to_list(new_number), answer)
    

N = list(map(int, list(input())))
answer_min = sys.maxsize
answer_max = 0

back_tracking(N, 0)
print(answer_min, answer_max)