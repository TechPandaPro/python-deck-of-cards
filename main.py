from deck import Deck
from hand import Hand

def main():
    deck = Deck()
    deck.fill()
    deck.shuffle()

    hand = Hand()

    print("Welcome to Card Deck Simulator!")

    done = False

    while not done:
        print()
        option = getOption(deck, hand)
        print()
        
        if option == "D":
            card = hand.drawFromDeck(deck)
            print("You drew a " + card.formatted() + ".")
        elif option == "P":
            print("Alright, great! Please specify the ID of a card to put back in the deck.")
            
            cardId = input()

            try:
                cardId = int(cardId)
            except ValueError:
                cardId = -1
            
            if cardId >= 1 and cardId <= len(hand.cards):
                cardId -= 1
                card = hand.cards[cardId]
                hand.putBack(deck, cardId)
                print("Your " + card.formatted() + " has been put back into a random spot in the deck.")
            else:
                print("That's not a valid card ID. Please try again or choose a different option.")
        elif option == "E":
            print("Alright! See you later!")
            done = True

def getOption(deck, hand):
    cardCount = len(hand.cards)

    if cardCount > 0:
        print("Your current hand (" + str(cardCount) + " total):")
        hand.print()
    else:
        print("Your hand is currently empty.")

    print()

    optionLetters = []
    optionDescriptions = []

    if len(deck.cards) > 0:
        optionLetters.append("D")
        optionDescriptions.append("Draw a card")
        
    if len(hand.cards) > 0:
        optionLetters.append("P")
        optionDescriptions.append("Put back a card")

    optionLetters.append("E")
    optionDescriptions.append("Exit")
        
    print("The deck has " + str(len(deck.cards)) + " cards left. What would you like to do?")

    for index, letter in enumerate(optionLetters):
        print(letter + ": " + optionDescriptions[index])
    
    option = input().upper()

    while option not in optionLetters:
        print("That's not a valid option! Please try again.")
        option = input().upper()

    return option

if __name__ == "__main__":
    main()
