def solution(number, limit, power):
    
    def getDivisors(num):
        divisors = {i for i in range(1, int(num**(1/2))+1) if not num%i}
        divisors.update({num//d for d in divisors})
        return divisors
    return sum([power if len(getDivisors(i)) > limit else len(getDivisors(i)) for i in range(1, number+1)])