from collections import deque

def solution(s):
    s = deque(s)
    answer = 0
    
    while len(s):
        cnt = 1
        x = s.popleft()
        while len(s):
            cnt = cnt + 1 if s.popleft() == x else cnt - 1
            if not cnt:
                answer += 1
                break
        if cnt >= 1 and not len(s):
            answer += 1
    return answer