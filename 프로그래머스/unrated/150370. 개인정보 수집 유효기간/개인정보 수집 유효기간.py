def solution(today, terms, privacies):
    answer = []
    
    def getIntDate(date):
        y, m, d = map(int, date.split('.'))
        return y * 12 * 28 + m * 28 + d
    
    today = getIntDate(today)
    
    dterms = dict()
    for term in terms:
        kind, period = map(str, term.split())
        dterms[kind] = today - int(period) * 28 + 1
    
    for idx, privacy in enumerate(privacies, start=1):
        date, kind = map(str, privacy.split())
        if dterms.get(kind) > getIntDate(date):
            answer.append(idx)
            
    return answer