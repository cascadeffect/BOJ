# 그냥 아무 생각 없이 팩토리얼로 풀어서 실패

import sys

# 이항계수(n, k) = 조합(n, k) = n!/(n-k)!k!

n, k = map(int, sys.stdin.readline().split())

def factorial(num):
  if num == 1:
    return 1
  return num * factorial(num-1) % 10007

print(int(factorial(n) / (factorial(n-k) * factorial(k))))