import sys

input = sys.stdin.readline

n = int(input())
count = [0] * 10000

for i in range(n):
  num = int(input())
  # 카운트 리스트: count[i-1]의 값은 숫자 i의 개수
  # e.g., 1의 개수는 count[0]에 저장
  count[num - 1] += 1

for i in range(10000):
  # count[i]가 0이 아니면, 즉 숫자 i+1의 개수가 0이 아니면
  if count[i] != 0:
    # count[i], 즉 숫자 i+1의 개수만큼 반복해서
    for j in range(count[i]):
      # 숫자 i+1 출력
      print(i + 1)