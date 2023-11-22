def solution(n):
    answer = n
    n = format(n, 'b')
    while True:
        answer += 1
        if str(format(answer, 'b')).count('1') == str(n).count('1'):
            return answer