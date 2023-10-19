from itertools import combinations

def solution(number):
    return sum(1 for nums in combinations(number, 3) if not sum(nums))