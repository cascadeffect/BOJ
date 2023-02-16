import sys

input = sys.stdin.readline

n = int(input())
info_list = [(list(map(int, input().split()))) for _ in range(n)]

rank_list = []

for i in range(n):
  my_rank = 1
  for j in range(n):
    if i != j and info_list[i][0] < info_list[j][0] and info_list[i][1] < info_list[j][1]:
      my_rank += 1
  rank_list.append(my_rank)

print(" ".join(map(str, rank_list)))