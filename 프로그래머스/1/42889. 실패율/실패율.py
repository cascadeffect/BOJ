from collections import Counter

def solution(N, stages):
    M = len(stages)
    counts = Counter(stages)
    answer = dict()
    for i in range(1, N+1):
        if M > 0:
            cnt = counts.get(i, 0)
            answer[i] = cnt / M
            M -= cnt
        else:
            answer[i] = 0
    return sorted(answer, key = lambda x : answer[x], reverse=True)