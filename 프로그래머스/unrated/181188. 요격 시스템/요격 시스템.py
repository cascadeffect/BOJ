def solution(targets):
    answer = 0
    # e > s 순으로 
    targets.sort(key = lambda x: [x[1], x[0]])
    
    prev_e = 0 # 정렬된 targets에서 이전 target의 e
    for now_s, now_e in targets:
        # prev_e보다 now_s가 큰 경우 겹치지 않기 때문에 요격 횟수 +1 && prev_e = now_e 
        if now_s >= prev_e:
            answer += 1
            prev_e = now_e
    return answer