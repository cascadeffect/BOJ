import sys

input = sys.stdin.readline

record = [list(input().split()) for _ in range(5)]
answer = 0

for start, end in record:
    start_hour, start_min = map(int, start.split(':'))
    end_hour, end_min = map(int, end.split(':'))
    if end_min >= start_min:
        answer += end_min - start_min + (end_hour - start_hour) * 60
    else:
        answer += 60 - start_min + end_min + (end_hour - start_hour - 1) * 60

print(answer)
