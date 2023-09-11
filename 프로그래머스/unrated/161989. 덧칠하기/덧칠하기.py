def solution(n, m, section):
    start = section[0]
    answer = 1
    for num in section:
        if num - start >= m:
            answer += 1
            start = num
    return answer