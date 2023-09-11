def solution(plans):
    answer = []
    stack = []
    
    plans = sorted(plans, key = lambda x : int(x[1].replace(':', '')))

    for plan in plans:
        hh, mm = map(int, plan[1].split(':'))
        plan[1] = hh * 60 + mm # 현 과제 시작시각(분)
        plan[2] = int(plan[2]) # 현 과제 남은시간(분)

        if len(stack):
            spare = plan[1] - stack[-1][1]
            while len(stack):
                if stack[-1][2] <= spare:
                    spare -= stack[-1][2]
                    answer.append(stack.pop()[0])
                else:
                    stack[-1][2] -= spare
                    break
        stack.append(plan)
        
    while len(stack):
        answer.append(stack.pop()[0])
    
    return answer