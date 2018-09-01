from math import factorial
from random import choices

'''
5 or more heads from 7 spins of a biased coin
'''

# simulation
population = ['heads', 'tails']
wgt = [6, 4]
cumwgt = [0.60, 1.00]

trial = lambda: choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >= 5

n = 100000
empirical_result = sum(trial() for i in range(n)) / n
print(empirical_result)


# analytic approach
def comb(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

ph = 0.6
# 5 heads out of 7 spins
ph_5 = ph ** 5 * (1-ph) ** 2 * comb(7, 5)
# 6 heads out of 7 spins
ph_6 = ph ** 6 * (1-ph) ** 1 * comb(7, 6)
# 7 heads out of 7 spins
ph_7 = ph ** 7 * (1-ph) ** 0 * comb(7, 7)

theoretical_result = ph_5 + ph_6 + ph_7
print(theoretical_result)
