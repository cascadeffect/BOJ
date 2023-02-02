import sys

input = sys.stdin.readline

t = int(input())
case = [list(map(int, input().split())) for _ in range(t)]

dic0 = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 4, '8': 7, '9': 6}

dic1 = {'0': '8', '3': '9', '5': ('6', '9'), '6': '8', '8': '9'}
dic2 = {'0': ('6', '7', '9'), '1': ('4', '7'), '2': ('3', '8'), '3': ('5', '8'), '4': ('7', '9'), '5': '8', '6': '9', '7': '9'}
dic3 = {'0': ('2', '3', '5'), '1': '3', '2': ('6', '9'), '3': ('4', '6', '7'), '4': ('5', '8'), '5': '7', '7': '8'}
dic4 = {'0': ('1', '4'), '1': '9', '2': '5', '4': '6', '6': '7'}
dic5 = {'1': ('2', '5', '8'), '2': ('4', '7')}
dic6 = {'1': '6'}

answer = []

def count_switch(before, after, digit):
    result = 0
    for i in range(digit):
        # 두 숫자가 같은 경우
        if before[i] == after[i]:
            continue
        # 두 숫자가 다른 경우
        key = min(before[i], after[i])
        value = max(before[i], after[i])

        if key in dic1 and value in dic1.get(key):
            result += 1
        elif key in dic2 and value in dic2.get(key):
            result += 2
        elif key in dic3 and value in dic3.get(key):
            result += 3
        elif key in dic4 and value in dic4.get(key):
            result += 4
        elif key in dic5 and value in dic5.get(key):
            result += 5
        elif key in dic6 and value in dic6.get(key):
            result += 6
    return result

for before, after in case:
    before_digit = len(str(before))
    after_digit = len(str(after))

    count = 0

    # 자릿수가 같은 경우
    if before_digit == after_digit:
        count = count_switch(str(before), str(after), before_digit)
    # 자릿수가 다른 경우
    elif before_digit > after_digit:
        count = count_switch(str(before)[(before_digit - after_digit):], str(after), min(before_digit, after_digit))
        for i in range(before_digit - after_digit):
            count += dic0.get(str(before)[i])
    elif before_digit < after_digit:
        count = count_switch(str(before), str(after)[(after_digit - before_digit):], min(before_digit, after_digit))
        for i in range(after_digit - before_digit):
            count += dic0.get(str(after)[i])

    answer.append(count)

for a in answer:
    print(a)