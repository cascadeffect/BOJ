import math

def solution(picks, minerals):
    answer = 0
    
    num_picks = sum(picks)
    if not num_picks:
        return answer
    
    num_minerals = num_picks * 5
    if len(minerals) > num_minerals:
        minerals = minerals[:num_minerals]
        
    cnt_minerals = [[0, 0, 0] for _ in range(math.ceil(len(minerals)/5))]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            cnt_minerals[i//5][0] += 1
        elif minerals[i] == 'iron':
            cnt_minerals[i//5][1] += 1
        else:
            cnt_minerals[i//5][2] += 1

    cnt_minerals.sort(key = lambda x : (-x[0], -x[1], -x[2]))
    
    idx = 0
    for d, i, s in cnt_minerals:
        while not picks[idx]:
            idx +=1
        if idx == 0:
            answer += d + i + s
        elif idx == 1:
            answer += 5*d + i + s
        elif idx == 2:
            answer += 25*d + 5*i + s
        picks[idx] -= 1

    return answer