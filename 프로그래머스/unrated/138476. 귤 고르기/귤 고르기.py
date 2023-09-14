from collections import Counter

def solution(k, tangerine):
    counter = sorted(Counter(tangerine).values(), key=lambda x: x)
    
    # 상동
    # tDict = dict()
    # for t in tangerine:
    #     if t in tDict:
    #         tDict[t] += 1
    #     else:
    #         tDict[t] = 1
    # tList = sorted(tDict.values(), key=lambda x: x)
    
    answer = 0
    while k > 0:
        k -= counter.pop()
        answer += 1
    return answer