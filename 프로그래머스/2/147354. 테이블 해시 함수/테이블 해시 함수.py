from functools import reduce

def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    return reduce(lambda x, y : x ^ y, [sum(d % i for d in data[i-1]) for i in range(row_begin, row_end+1)])