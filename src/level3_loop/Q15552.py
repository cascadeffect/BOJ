import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
  A, B = [int(i) for i in input().split(' ')]
  print(A+B)