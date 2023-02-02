import sys

input = sys.stdin.readline

numList = []
for i in range(10):
  numList.append(int(input())%42)

numList = set(numList)

print(len(numList))