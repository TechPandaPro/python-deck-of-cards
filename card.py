class Card:
    def __init__(self, suit, rank):
        # for some card games, knowing the value and/or suit would be important which is why here I keep them separate

        self.rank = rank
        self.suit = suit

    def formatted(self):
        return str(self.rank).capitalize() + " of " + self.suit.capitalize()
