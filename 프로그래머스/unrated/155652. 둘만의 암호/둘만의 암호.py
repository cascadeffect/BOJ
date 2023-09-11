def solution(s, skip, index):
    answer = ''
    for c in s:
        now = c
        count = 0
        while count < index:
            chg = ord(now)+1
            if chg > 122:
                chg = 97
            chg = chr(chg)
            if chg not in skip:
                count += 1
            now = chg
        answer += chg
    return answer