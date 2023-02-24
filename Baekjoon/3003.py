import sys

input = sys.stdin.readline

correct_pieces = [1, 1, 2, 2, 2, 8]
given_pieces = list(map(int, input().split()))
result = []

for i in range(6):
  if given_pieces[i] != correct_pieces[i]:
    result.append(str(correct_pieces[i]- given_pieces[i]))
  else:
    result.append('0')

print(' '.join(result))