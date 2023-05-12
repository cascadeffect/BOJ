def recursive_function(i):
  # 종료 조건 필수
  if i == 100:
    return
  print(f'{i}번째 재귀 함수에서 {i+1}번째 재귀 함수를 호출합니다.')
  recursive_function(i+1)
  print(f'{i}번째 재귀 함수를 종료합니다.')

recursive_function(1)