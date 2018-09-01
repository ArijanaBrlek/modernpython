'''
Bootstrapping to estimate the confidence interval on a sample of data
'''

from random import choices
from statistics import mean, stdev

timings = [
    7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98,
    8.31, 9.06, 7.06, 7.67, 10.02, 6.87, 9.07
]

print(sorted(timings))
print(mean(timings))
print(stdev(timings))

# Build a 90% confidence interval


def bootstrap(data):
    return choices(data, k=len(data))


bootstrapped_timings = bootstrap(timings)
print(sorted(bootstrapped_timings))
print(mean(bootstrapped_timings))
print(stdev(bootstrapped_timings))

n = 10000
means = sorted(mean(bootstrap(timings)) for i in range(n))
print(mean(means))

confidence_limit = round(n * 0.05)

print(f'The observed mean of {mean(timings)}')
print(f'Falls in a 90% confidence interval from {means[confidence_limit] :.1f} to {means[-confidence_limit] :.1f}')
