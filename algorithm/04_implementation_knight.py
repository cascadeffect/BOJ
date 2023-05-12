import sys

input_data = input()

x = int(ord(input_data[0])) - int(ord('a')) + 1
y = int(input_data[1])
directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
count = 0

for direction in directions:
  nx = x + direction[0]
  ny = y + direction[1]
  if 1 <= nx <= 8 and 1 <= ny <= 8:
    count += 1

print(count)