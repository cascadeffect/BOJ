from collections import Counter

def solution(k, tangerine):
    counter = sorted(Counter(tangerine).values(), key=lambda x: x)
    answer = 0
    while k > 0:
        k -= counter.pop()
        answer += 1
    return answer