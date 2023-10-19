from itertools import permutations

def solution(k, dungeons):
    answer = []
    for permutation in permutations(range(len(dungeons))):
        ftg = k
        cnt = 0
        for idx in permutation:
            if ftg >= dungeons[idx][0]:
                ftg -= dungeons[idx][1]
                cnt += 1
        answer.append(cnt)
    return max(answer)