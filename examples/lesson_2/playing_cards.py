from collections import Counter
from random import sample

'''
Deal 20 playing cards without replacement (16 tens, 36 low)
'''

deck = Counter(tens=16, low=36)
deck = deck.elements()

deal = sample(deck, 52)
remainder = deal[20:]
print(Counter(remainder))
