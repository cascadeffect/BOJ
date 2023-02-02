import sys

input = sys.stdin.readline

m, n, k = map(int, input().split()) # 비밀 메뉴 버튼 조작 수, 사용자 버튼 조작 수, 총 버튼 수
manual = "".join(input().split())
order = "".join(input().split())

if m <= n:
    if manual in order:
        print('secret')
    else:
        print('normal')
else:
    print('normal')