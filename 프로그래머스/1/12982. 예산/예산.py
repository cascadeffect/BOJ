def solution(d, budget):
    s = 0
    for i, n in enumerate(sorted(d)):
        if s+n > budget:
            return i
        s += n
    return len(d)