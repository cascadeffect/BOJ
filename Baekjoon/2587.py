import sys

nums = [int(input()) for _ in range(5)]
nums.sort()
print(int(sum(nums) / len(nums)))
print(nums[len(nums) // 2])