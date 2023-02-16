import sys

input = sys.stdin.readline

t = int(input())

# a%b와 b의 GCD == a와 b의 GCD (유클리드 호제법)
def GCD(a, b):
  while b > 0:
    a, b = b, a%b
  return a

# a*b = GCD*LCM
def LCM(a, b):
  return a * b // GCD(a, b)

for _ in range(t):
  a, b = (map(int, input().split()))
  print(LCM(a, b))
  