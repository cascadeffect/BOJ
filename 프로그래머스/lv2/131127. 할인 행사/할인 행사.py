from collections import Counter

def solution(want, number, discount):
    
    if not set(want) <= set(discount):
        return 0
    
    dictionary = dict(zip(want, number))
    
    return len([1 for i in range(len(discount)-9) if dictionary == Counter(discount[i:i+10])])