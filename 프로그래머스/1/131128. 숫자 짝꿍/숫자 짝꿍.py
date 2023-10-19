def solution(X, Y):
    X, Y = sorted(X, reverse=True), sorted(Y, reverse=True)
    i = j = 0
    answer = ''
    
    while i < len(X) and j < len(Y):
        if X[i] == Y[j]:
            answer += X[i]
            if answer == '0':
                return '0'
            i += 1
            j += 1
        elif X[i] > Y[j]:
            if X[i] == X[-1]:
                break
            i += 1
        else:
            if Y[j] == Y[-1]:
                break
            j += 1
    
    return answer or '-1'