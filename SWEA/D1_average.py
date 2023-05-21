T = int(input())
for case in range(1, T + 1):
    nums = list(map(int, input().split()))
    avg = round(sum(nums) / 10)
    print(f'#{case} {avg}')