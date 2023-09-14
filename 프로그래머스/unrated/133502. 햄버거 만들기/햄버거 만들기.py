def solution(ingredient):
    answer = 0
    burger = []

    def isBurger():
        for i in range(3, 0, -1):
            if i != burger[i-4]:
                return False
        return True
    
    for i in ingredient:
        if i == 1 and len(burger) >= 3 and isBurger():
            for _ in range(3):
                burger.pop()
            answer += 1
            continue
        burger.append(i)

    return answer