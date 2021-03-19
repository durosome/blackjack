import random


def create_deck():
    card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suits = ['♠', '♦', '♥', '♣']
    deck = []

    for suit in card_suits:
        for value in card_values:
            deck.append(value + suit)

    return deck


class Dealer:
    """
    game logic class, created for rule the game
    """

    def __init__(self):  # initialization
        pass

    def rule_game(self):  # rule game
        pass


class Table:
    def __init__(self, slot_numbers):
        self.slot_numbers = slot_numbers
        self.slots = [Player_Slot(f"slot_{i}") for i in range(slot_numbers)]

    def assign_id(self):  # makes unique id for new slot, while new player slot will be created
        pass


class Player_Slot():
    def __init__(self, slot_id: str):
        self.slot_id = slot_id
