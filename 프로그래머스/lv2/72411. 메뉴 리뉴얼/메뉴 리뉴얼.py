from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for num in course:
        combos = []
        for order in orders:
            combos += [''.join(sorted(menu)) for menu in combinations(order, num)]
        if not len(combos):
            continue
        combos = Counter(combos)
        maximum = max(combos.values())
        if maximum <= 1:
            continue
        answer.extend([new for new in filter(lambda x: combos.get(x) == maximum, combos.keys())])
    return sorted(answer)