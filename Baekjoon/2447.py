import sys

n = int(sys.stdin.readline())

def draw(num):
  if num == 1:
    return ['*']
  
  stars = draw(num//3)
  result = []

  for star in stars:
    result.append(star * 3)
  for star in stars:
    result.append(star + ' '*(num//3) + star)
  for star in stars:
    result.append(star * 3)

  return result

print('\n'.join(draw(n)))