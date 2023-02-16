import sys

while True:
  coordinate = list(map(int, sys.stdin.readline().split()))
  if coordinate == [0, 0, 0]:
    break;
  coordinate.sort()
  if coordinate[0] ** 2 + coordinate[1] ** 2 == coordinate[2] ** 2:
    print('right')
  else:
    print('wrong')