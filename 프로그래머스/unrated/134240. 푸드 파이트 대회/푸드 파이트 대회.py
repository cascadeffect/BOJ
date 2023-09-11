def solution(food):
    answer = ''.join([str(idx) * (elm//2) for idx, elm in enumerate(food)])
    return answer + '0' + answer[::-1]