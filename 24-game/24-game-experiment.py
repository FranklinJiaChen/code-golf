"""
eval has to be OP if I figure out how to get it to work without timing out
"""
from itertools import*
operator = '+-*/'

for i in combinations_with_replacement(range(1,14),4):
    for a,b,c,d in permutations(i):
        if 24 in [eval(f'{a}{e}{b}{f}{c}{g}{d}') for e,f,g in product(operator,repeat=3)]:print(*i);break