import random


def create_deck():
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = ['♠', '♦', '♥', '♣']
    deck = []

    for suit in card_suits:
        for value in card_values:
            deck.append(value + suit)

    return deck


class Table:
    def __init__(self):
        player_slot = 7

    def create_dealer(self):
        class Dealer:
            def __init__(self):
                self.deck = [1, 2, 3]
                self.deck = create_deck()
                random.shuffle(self.deck)

        self.dealer = Dealer()



table = Table()
table.create_dealer()
print(table.dealer.deck)
