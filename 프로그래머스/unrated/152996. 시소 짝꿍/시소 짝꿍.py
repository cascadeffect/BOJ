def solution(weights):
    
    dict1 = dict()
    
    for w in weights:
        if w in dict1:
            dict1[w] += 1
        else:
            dict1[w] = 1
    
    dict2 = dict1.copy()
    conditions = {1/2, 2/3, 3/4, 1}
    answer = 0
    
    for ki, vi in dict1.items():
        if vi >= 2:
            answer += vi * (vi-1) / 2
        del dict2[ki]
        for kj, vj in dict2.items():
            if min(ki, kj) / max(ki, kj) in conditions:
                answer += vi * vj
                
    return answer