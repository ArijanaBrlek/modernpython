from random import sample
from statistics import median

'''
Probability that the median of 5 samples falls a middle quartile
'''
# m = sorted(sample(range(100000), 5))[2]

n = 100000
trial = lambda: n // 4 < median(sample(range(100000), 5)) <= 3 * n // 4

empirical_result = sum(trial() for i in range(n)) / n
print(empirical_result)
