import sys

n = int(sys.stdin.readline())

# 하노이의 탑
# n: 원판 개수, k: 옮긴 횟수
# n=1 -> k=1 (+ 2^0)
# n=2 -> k=3 (+ 2^1)
# n=3 -> k=7 (+ 2^2)
# n=4 -> k=15 (+ 2^3)
# n=5 -> k=31 (+ 2^4)

# n=홀수일 때: 1->3 시작?
# n=짝수일 때: 1->2 시작?

def hanoi():
  return

k = 0
for i in range(1, n+1):
  k += (2 ** (i-1))

print(k)
# hanoi(n, 1, 3, 2)