def solution(s):
    
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = [str(i) for i in range(10)]
    words = dict(zip(eng, num))
    tmp = ''
    answer = ''
    for i in s:
        if i in num:
            answer += i
        else:
            tmp += i
            if tmp in words:
                answer += words[tmp]
                tmp = ''
            
    return int(answer)