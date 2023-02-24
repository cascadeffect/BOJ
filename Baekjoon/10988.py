import sys

input = sys.stdin.readline

str = input().rstrip()

def isPalindrome(str):
  for l in range(int(len(str) / 2)):
    if str[l] != str[-(l+1)]:
      return False
  return True

print(1 if isPalindrome(str) else 0)