import sys

t = int(sys.stdin.readline()) # 테케 개수
for i in range(t):
  a = list(map(int, sys.stdin.readline().split()))
  a.sort()
  print(a[-3])