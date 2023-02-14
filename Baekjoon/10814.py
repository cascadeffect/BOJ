import sys

input = sys.stdin.readline

n = int(input())
members = [input().split() for _ in range(n)]

sorted_members = sorted(members, key=lambda x: int(x[0]))

for age, name in sorted_members:
  print(int(age), name)