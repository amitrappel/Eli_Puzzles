from itertools import product
from random import choice
import pandas as pd

genders = ['m', 'f']
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
combos = list(product(genders, days))

N = 10000
conditional_history = [tup for tup in history if ('m', 'Tuesday') in tup]

def is_two_boys(tup):
    return tup[0][0] == 'm' and tup[1][0] == 'm'
    
conditional_ps = []

for n in range(100, N, 10):
    conditional_history = [tup for tup in history if ('m', 'Tuesday') in tup]
    conditional_ps.append(sum([is_two_boys(tup) for tup in conditional_history]) / 
        len(conditional_history))
        
probs = pd.Series(conditional_ps, name='Conditional');
probs.plot(xlabel='$N$ (Number of families tested)', ylabel='Probability of 2 boys');