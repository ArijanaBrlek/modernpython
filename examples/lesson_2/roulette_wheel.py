from collections import Counter
from random import choices

'''
Six roulette wheel spins
'''

population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
game = Counter(choices(population, k=6))
print(game)

game = Counter(choices(['red', 'black', 'green'], [18, 18, 2], k=6))
print(game)
