def solution(numbers, hand):
    lnums = (1, 4, 7)
    rnums = (3, 6, 9)
    mnums = (2, 5, 8, 0)
    left, right = (3, 0), (3, 2)
    answer = ''
    
    for number in numbers:
        if number in lnums:
            left = (lnums.index(number), 0)
            answer += 'L'
        elif number in rnums:
            right = (rnums.index(number), 2)
            answer += 'R'
        else:
            ldist = abs(mnums.index(number)-left[0]) + (1-left[1])
            rdist = abs(right[0]-mnums.index(number))+ (right[1]-1)
            if ldist == rdist:
                if hand == 'left':
                    left = (mnums.index(number), 1)
                    answer += 'L'
                else:
                    right = (mnums.index(number), 1)
                    answer += 'R'
            elif ldist < rdist:
                left = (mnums.index(number), 1)
                answer += 'L'
            else:
                right = (mnums.index(number), 1)
                answer += 'R'
    return answer