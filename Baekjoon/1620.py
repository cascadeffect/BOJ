import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pokemon_list = {}

for i in range(1, n+1):
  pokemon = input().rstrip()
  pokemon_list[i] = pokemon
  pokemon_list[pokemon] = i

for _ in range(m):
  # 문제가 문자열인 경우
  question = input().rstrip()
  if question.isalpha():
    print(pokemon_list[question])
  # 문제가 숫자인 경우
  else:
    print(pokemon_list[int(question)])