import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_str = {input().rstrip() for _ in range(n)}
m_str = [input().rstrip() for _ in range(m)]

count = 0

for str in m_str:
    if str in n_str:
      count += 1

print(count)