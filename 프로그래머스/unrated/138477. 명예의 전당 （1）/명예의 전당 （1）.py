import heapq

def solution(k, score):
    answer = []
    hof = []
    if k < len(score):
        for i in range(k):
            heapq.heappush(hof, score[i])
            answer.append(hof[0])
        for i, e in enumerate(score[k:], start=k):
            heapq.heappushpop(hof, e)
            answer.append(hof[0])
    else:
        for e in score:
            heapq.heappush(hof, e)
            answer.append(hof[0])
    return answer