from itertools import combinations

def solution(numbers):
    return sorted(list(set(sum(combo) for combo in combinations(numbers, 2))))