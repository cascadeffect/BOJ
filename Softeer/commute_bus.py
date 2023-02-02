import sys

input = sys.stdin.readline

n = int(input())
buses = list(map(int, input().split()))

answer = 0

# a3 < a1 < a2
for i in range(n-2):
    # a1이 1이 아닐 때
    if buses[i] != 1:
        # a1 뒤에서
        for j in range(i+1, n-i):
            # a1보다 큰 a2를 찾았을 때
            if buses[i] < buses[j]:
                # a1보다 작은 a3 후보군과 a2 뒤의 숫자들을 비교하여 개수 카운트
                # 1번 방법
                answer += len(set(range(1, buses[i])) & set(buses[j+1:]))
#                 # for k in range(1, buses[i]):
#                     # 2번 방법
#                     if k in buses[j+1:]:
#                         answer += 1
#                     # 3번 방법
#                         answer += buses[j+1:].count(k)

print(answer)