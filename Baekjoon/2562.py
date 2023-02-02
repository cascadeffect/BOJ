import sys

input = sys.stdin.readline

numList = []
for i in range(9):
  numList.append(int(input()))

maxNum = max(numList)
print(maxNum)
print(numList.index(maxNum)+1)