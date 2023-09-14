def solution(order):
    answer = 0
    boxes = [i for i in range(len(order), 0, -1)]
    stack = []
        
    while len(boxes) or len(stack):
        if len(boxes) and boxes[-1] == order[answer]:
            boxes.pop()
            answer += 1
        elif len(stack) and stack[-1] == order[answer]:
            stack.pop()
            answer += 1
        elif not len(boxes) and len(stack) and stack[-1] != order[answer]:
            break
        else:
            stack.append(boxes.pop())

    return answer