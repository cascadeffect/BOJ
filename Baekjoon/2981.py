# 실패

import sys

input = sys.stdin.readline

n = int(input())
num_list = [int(input()) for _ in range(n)]

m_list = []

for m in range(2, max(num_list)+1):
  remainder = []
  for num in num_list:
    remainder.append(num % m)
  if len(set(remainder)) == 1:
    m_list.append(str(m))

print(' '.join(m_list))