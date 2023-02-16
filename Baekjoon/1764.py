import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_set = {input().rstrip() for _ in range(n)}
m_set = {input().rstrip() for _ in range(m)}
nm_list = sorted(list(n_set & m_set))

print(len(nm_list))
for nm in nm_list:
  print(nm)