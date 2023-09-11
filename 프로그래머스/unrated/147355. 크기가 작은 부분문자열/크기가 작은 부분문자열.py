from collections import deque

def solution(t, p):
    t = deque(t)
    tmp = deque(t.popleft() for _ in range(len(p)-1))
    p = int(p)
    answer = 0
    while len(t):
        tmp.append(t.popleft())
        if int(''.join(tmp)) <= p:
            answer += 1
        tmp.popleft()
    return answer