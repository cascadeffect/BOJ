def solution(storey):
    answer = 0
    
    while storey:
        r = storey % 10
        
        if r > 5:
            num = 10 - r
        elif r < 5:
            num = -r
        elif len(str(storey)) >= 2 and int(str(storey)[-2]) >= 5:
            num = 10 - r
        else:
            num = -r

        answer += abs(num)
        storey = (storey+num) // 10
        
    return answer