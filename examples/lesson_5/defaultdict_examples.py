from collections import defaultdict
from pprint import pprint

d = defaultdict(list)
d['raymond'].append('red')
d['rachel'].append('blue')
d['matthew'].append('yellow')

d['raymond'].append('mac')
d['rachel'].append('pc')
d['matthew'].append('vtech')

pprint(dict(d))

# model one-to-many: dict(one, list_of_many)
e2s = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio': ['tres'],
    'free': ['libre', 'gratis']
}

pprint(e2s)

s2e = defaultdict(list)
for eng, spanwords in e2s.items():
    for span in spanwords:
        s2e[span].append(eng)

pprint(s2e)

# one-to-one
e2s = dict(one='uno', two='dos', three='tres')
s2e = {span: eng for eng, span in e2s.items()}

