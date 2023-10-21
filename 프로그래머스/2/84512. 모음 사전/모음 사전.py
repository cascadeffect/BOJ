from itertools import product

solution = lambda word: sorted([''.join(p) for i in range(1, 6) for p in list(product(['A', 'E', 'I', 'O', 'U'], repeat=i))]).index(word) + 1