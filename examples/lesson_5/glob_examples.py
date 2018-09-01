import csv

# print(glob.glob('../../*.py'))  # global wildcard expansion
from collections import Counter
from pprint import pprint

with open('../../congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    print(f.read())

it = iter('abcdefgh')
print(next(it))  # a
print(next(it))  # b
list(it)  # cdefgh

with open('../../congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)

t = ('Raymond', 'Hettinger', 54, 'python@rcn.com')
type(t)
len(t)
fname, lname, age, email = t

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow'.split()
cities = 'austin dallas austin huston chicago dallas austin'.split()

# loop idioms
for i, name in enumerate(names, start=1):
    print(i, name)

for color in reversed(colors):
    print(color)

for name, color in zip(names, colors):
    print(name, color)

for color in sorted(colors, key=len):
    print(color)

for color in sorted(colors, key=lambda color: color[-1]):
    print(color)

for city in sorted(set(cities)):
    print(city)

for i, city in enumerate(map(str.upper, reversed(sorted(set(cities))))):
    print(i, city)

# counter
c = Counter()
c['red'] += 1
c['red'] += 1
c['blue'] += 1
pprint(c)

print(c.most_common(2))
print(list(c.elements()))
