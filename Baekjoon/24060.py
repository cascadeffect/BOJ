import sys

input = sys.stdin.readline

n, k = int(input())
array = list(map(int, input().split()))

def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  merge_sort(left)
  merge_sort(right)
  merge(left, right)

def merge(left, right):
    # i = 0
    # j = len(left)
    # k = 1
    # while i <= len(left) and j < len(right):
    #   if left[i] < right[j]:
    #     a[k] = left[i]
    #     i += 1
    #     k += 1