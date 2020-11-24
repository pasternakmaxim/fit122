from collections import namedtuple

Card = namedtuple('Card','sign,value')
SIGNS = ['Hearts','Diamonds','Spades','Clubs']


class Deck:
	def __init__(self):
		self.cards = [Card(sign, value) for sign in SIGNS for value in range(2,
																			11) +
						'J Q K A'.split()]

	def __repr__(self):
		return srt([str(card) for card in self.cards])

	def __len__(self):
		return len(self.cards)

	def __getitem__(self, item):
		return self.cards[item]

	def __setitem__(sefl, key, value):
		self.cards[key] = value


deck = Deck()

print (deck[11])

print (len(deck))

print (deck[13:17])

import random

random.shuffle(deck)	