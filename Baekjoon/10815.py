import sys

input = sys.stdin.readline

input()
cards = set(map(int, input().split())) # in 연산자를 수행할 자료구조를 list 대신 set으로 설정
input()
numbers = list(map(int, input().split()))

for number in numbers:
  if number in cards:
    print(1, end=" ")
  else:
    print(0, end=" ")