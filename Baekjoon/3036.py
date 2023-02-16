import sys

n = int(input())
nums = list(map(int, input().split()))

def GCD(a, b):
  if b > a:
    a, b = b, a
  while b > 0:
    a, b = b, a % b
  return a

for i in range(1, n):
  gcd = GCD(nums[0], nums[i])
  print(f'{nums[0]//gcd}/{nums[i]//gcd}')