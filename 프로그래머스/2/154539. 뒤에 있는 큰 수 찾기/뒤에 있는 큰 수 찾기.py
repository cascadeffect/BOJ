def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack:
            if stack[-1] > numbers[i]:
                answer[i] = stack[-1]
                break
            else:
                stack.pop()
        stack.append(numbers[i])
    return answer