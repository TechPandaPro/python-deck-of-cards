import random
from card import Card

suits = [ "clubs", "diamonds", "hearts", "spades" ]
ranks = [ "ace", *range(2, 11), "jack", "queen", "king" ]

class Deck:
    def __init__(self):
        self.cards = []

    def fill(self):
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
                
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def insert(self, card):
        self.cards.insert(random.randint(0, len(self.cards)), card)
