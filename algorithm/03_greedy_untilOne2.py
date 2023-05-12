import sys

n, k = map(int, sys.stdin.readline().split())
count = 0

# N이 K 이상이라면 K로 계속 나누기
while True:
  # N이 K의 배수가 될 떄까지 1씩 빼기
  target = (n // k) * k
  count += n - target
  n = target
  # N이 K보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # K로 나누기
  count += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
count += n - 1

print(count)