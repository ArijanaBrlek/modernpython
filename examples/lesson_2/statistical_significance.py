'''
Statistical significance of the difference of two means
'''

from random import shuffle
from statistics import mean

drug = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]

print(mean(drug))
print(mean(placebo))

obs_diff = mean(drug) - mean(placebo)
print(obs_diff)

comb = drug + placebo
nd = len(drug)


def trial():
    shuffle(comb)
    drug = comb[:nd]
    placebo = comb[nd:]

    new_diff = mean(drug) - mean(placebo)
    return new_diff > obs_diff


n = 10000

# likelihood that the outcome was solely due to chance
print(sum(trial() for i in range(n)) / n)
