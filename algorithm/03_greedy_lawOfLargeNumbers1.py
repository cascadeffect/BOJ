import sys

input = sys.stdin.readline

n, m, k = map(int, input().split()) # n: 자연수 개수, m: 더하는 횟수, k: 연속 제한 횟수 (k <= m)
nums = list(map(int, input().split()))
answer = 0

nums = sorted(nums, reverse=True)
first = nums[0]
second = nums[1]

# NOTE: 주어진 m을 직접 건드리기
while True:
  for j in range(k):
    if m == 0:
      break
    answer += first
    m -= 1
  if m == 0:
    break
  answer += second
  m -= 1

print(answer)

# 풀이
# 입력값 중에서 가장 큰 수와 두 번째로 큰 수만 저장하면 된다.
# 연속으로 더할 수 있는 횟수는 최대 K번이므로 가장 큰 수를 K번 더하고 두 번째로 큰 수를 한 번 더하는 연산을 반복하면 된다.