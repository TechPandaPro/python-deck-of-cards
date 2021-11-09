class Hand:
    def __init__(self):
        self.cards = []

    def drawFromDeck(self, deck):
        card = deck.draw()
        self.cards.append(card)
        return card

    def putBack(self, deck, index):
        card = self.cards[index]
        self.cards.remove(card)
        deck.insert(card)

    def print(self):
        for index, card in enumerate(self.cards):
            print(str(index+1) + ") " + card.formatted())
