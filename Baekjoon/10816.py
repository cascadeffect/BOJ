import sys

input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))

card_dict = {}

for card in card_list:
  if card not in card_dict:
    card_dict[card] = 1
  else:
    card_dict[card] += 1

m = int(input())
quest_list = list(map(int, input().split()))

result = []

for quest in quest_list:
  result.append(str(card_dict[quest]) if quest in card_dict else '0')

print(' '.join(result))