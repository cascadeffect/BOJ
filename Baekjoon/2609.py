import sys

a, b = map(int, sys.stdin.readline().split(' '))

m = min(a, b)

gcd = 1 # 최대공약수
lcm = a * b # 최소공배수

for i in range(m, 0, -1):
  if a % i == 0 and b % i == 0:
    gcd = i
    break

lcm = int(a * b / gcd)

print(gcd)
print(lcm)