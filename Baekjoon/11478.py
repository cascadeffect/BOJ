import sys

s = sys.stdin.readline().rstrip()

sub = set()

for i in range(len(s)):
  for j in range(i+1, len(s)+1):
    sub.add(s[i:j])

print(len(sub))