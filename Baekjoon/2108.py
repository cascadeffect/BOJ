import sys

input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))

nums.sort()

# 산술평균 계산 & 출력
print(round(sum(nums) / n))
# 중앙값 계산 & 출력
print(nums[n // 2])

# 최빈값 계산
now_count = 1
max_count = 1
prev_num = 0
mode = []
for i in range(n+1):
  if i == 0:
    prev_num = nums[i]
  elif i == n:
    if now_count > max_count:
      mode = [prev_num]
    elif now_count == max_count:
        mode.append(prev_num)
  else:
    # 이전 숫자와 현재 숫자가 다르면
    if nums[i] != prev_num:
      # 이전 숫자 카운팅이 현재까지 최대 카운팅보다 크면
      if now_count > max_count:
        # 이전 숫자로 최빈값 초기화
        mode = [prev_num]
        # 이전 숫자 카운팅으로 최대 카운팅 초기화
        max_count = now_count
      # 이전 숫자 카운팅이 현재까지 최대 카운팅과 같으면
      elif now_count == max_count:
        # 최빈값 후보 리스트에 이전 숫자 삽입
        mode.append(prev_num)
      # 이전 숫자 카운팅 초기화
      now_count = 1
    # 이전 숫자와 현재 숫자가 같으면
    else:
      # 현재(=이전) 숫자 카운팅 + 1
      now_count += 1
    # 현재 숫자로 이전 숫자 초기화
    prev_num = nums[i]

# 최빈값 출력
if len(mode) == 1:
  print(mode[0])
else:
  print(mode[1])

# 범위 계산 & 출력
print(nums[n-1] - nums[0])