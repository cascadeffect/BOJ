import sys

input = sys.stdin.readline

a_count, b_count = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

print(len((a_set - b_set) | (b_set - a_set)))