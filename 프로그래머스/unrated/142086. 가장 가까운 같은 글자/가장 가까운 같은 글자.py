def solution(s):
    answer = []
    d = dict()
    for idx, char in enumerate(s):
        if char in d:
            answer.append(idx-d.get(char))
        else:
            answer.append(-1)
        d[char] = idx
    return answer