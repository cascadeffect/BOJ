import sys

input = sys.stdin.readline

n = int(input())
words = list(set([input().rstrip() for _ in range(n)]))

sorted_words = sorted(words, key = lambda word: (len(word), word))

for word in sorted_words:
  print(word)