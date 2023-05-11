import sys

input = sys.stdin.readline

n, m, k = map(int, input().split()) # n: 자연수 개수, m: 더하는 횟수, k: 연속 제한 횟수 (k <= m)
nums = list(map(int, input().split()))
answer = 0

nums = sorted(nums, reverse=True)
first = nums[0]
second = nums[1]

# 가장 큰 수가 더해지는 횟수
count = m // (k+1) * k + m % (k+1)

answer += first * count # 가장 큰 수 더하기
answer += second * (m-count) # 두 번째로 큰 수 더하기

print(answer)

# 풀이
# M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받을 것이다.
# 간단한 수학적 아이디어를 이용해 더 효율적으로 문제를 해결해보자.
# 반복되는 수열에 대해 파악해야 한다.
# 가장 큰 수와 두 번째로 큰 수가 더해질 때는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
# 반복되는 수열의 길이는 (K+1)이다.
# 따라서 M을 (K+1)로 나눈 몫이 수열이 반복되는 횟수가 되고, 다시 여기에 K를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
# 이때 M이 (K+1)로 나누어 떨어지지 않는 경우도 고려해야 한다.
# 그럴 대는 M을 (K+1)로 나눈 나머지만큼 가장 큰 수가 더해지므로 이를 고려해야 한다.
# 즉, 가장 큰 수가 더해지는 횟수는 M // (K+1) * K + M % (K+1) 이다.