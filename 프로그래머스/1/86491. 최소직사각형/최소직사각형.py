from functools import reduce
solution = lambda sizes: reduce(lambda w, h: w * h, map(max, zip(*map(sorted, sizes))))
