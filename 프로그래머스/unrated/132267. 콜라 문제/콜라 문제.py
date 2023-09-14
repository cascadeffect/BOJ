def solution(a, b, n):
    answer = 0
    while n >= a:
        num = n // a
        old = num * a
        n -= old
        new = old * b // a
        n += new
        answer += new
    return answer