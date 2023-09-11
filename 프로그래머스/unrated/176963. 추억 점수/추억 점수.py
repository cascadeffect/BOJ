def solution(name, yearning, photo):
    answer = []
    ny = {name[i] : yearning[i] for i in range(len(yearning))}

    for p in photo:
        tmp = 0
        for n in p:
            tmp += ny[n] if ny.get(n) != None else 0
        answer.append(tmp)
        
    return answer