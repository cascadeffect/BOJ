def solution(s):
    answer = 0
    
    for b in s:
        answer = answer + 1 if b == '(' else answer - 1
        if answer < 0:
            return False
    
    return answer == 0