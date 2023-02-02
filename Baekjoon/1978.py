import sys
import math

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
count = 0

def isPrime(num):
    if num == 1:
      return False # 소수 X
    for i in range(2, int(math.sqrt(num) + 1)):
      if num % i == 0:
        return False # 소수 X
    return True # 소수 O

if n > 0:
  for num in nums:
    if isPrime(num):
      count += 1

print(count)