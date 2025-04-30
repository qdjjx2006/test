# adapted from Alex Martelli's example in "Re-learning Python"
# http://www.aleax.it/Python/accu04_Relearn_Python_alex.pdf
# (slide 41) Ex: lines-by-word file index

# BEGIN INDEX0
"""Build an index mapping word -> list of occurrences"""


##import sys
##import re
##
##WORD_RE = re.compile(r'\w+')
##
##index = {}
##with open(sys.argv[0], encoding='utf-8') as fp:
##    for line_no, line in enumerate(fp, 1):
##        for match in WORD_RE.finditer(line):
##            word = match.group()
##            column_no = match.start()+1
##            location = (line_no, column_no)
##            # this is ugly; coded like this to make a point
##            occurrences = index.get(word, [])  # <1>
##            occurrences.append(location)       # <2>
##            index[word] = occurrences          # <3>
##
### print in alphabetical order
##for word in sorted(index, key=str.upper):  # <4>
##    print(word, index[word])
### END INDEX0

import sys
import collections
import os
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]




Card = collections.namedtuple('Card1', ['rank', 'suit'])
C7 = Card('7','spade')
deck = FrenchDeck()
Cx = random.choice(deck)

Cx = random.choice(deck)
print(Cx)

print('\n')

#for card in deck:
for card in reversed(deck):
    print(card)
    
print('\n')

print(deck[:3])
print(deck[12::13])
print('\n')

suit_values = dict(spades=3,hearts=2,diamonds=1,clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)


















