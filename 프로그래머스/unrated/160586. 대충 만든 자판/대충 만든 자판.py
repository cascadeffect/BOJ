def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for char in target:
            min_index = 100
            for key in keymap:
                index = key.find(char)
                if index != -1 and index < min_index:
                    min_index = index
                    if min_index == 0:
                        break
            if min_index < 100:
                count += min_index + 1
            else:
                count = -1
                break
        answer.append(count)
    return answer