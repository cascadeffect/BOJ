import sys

input = sys.stdin.readline

factor_cnt = int(input())
factor_list = list(map(int, input().split()))

print(max(factor_list) * min(factor_list))