import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]

c = [[str(a[i][j] + b[i][j]) for j in range(m)] for i in range(n)]

for i in range(n):
    print(' '.join(c[i]))