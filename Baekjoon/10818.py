import sys

input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))

print(min(numList), max(numList))