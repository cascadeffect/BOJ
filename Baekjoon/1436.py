import sys

n = int(sys.stdin.readline())

number = 666
series = 1

while(True):
  if series == n:
    break
  number += 1
  if '666' in str(number):
    series += 1

print(number)