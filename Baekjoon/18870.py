import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(list(set(nums)))

num_dict = {sorted_nums[i] : i for i in range(len(sorted_nums))}

for num in nums:
  print(num_dict[num], end=' ')