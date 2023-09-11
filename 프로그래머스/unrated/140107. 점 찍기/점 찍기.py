def solution(k, d):
    return sum([int((d**2 - x**2)**(1/2) // k) + 1 for x in range(0, d+1, k)])