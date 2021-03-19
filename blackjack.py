import random


class Dealer:
    """
    game logic class, created for rule the game
    players - list of players, inputted by user interface !blackjack
    """

    def __init__(self):  # initialization
        pass

    def rule_game(self, players: list):  # rule game
        self.players = players
        self.slots_number = 7
        self.table = Table(self.slots_number)
        self.slots = []

        for self.slot_id in range(0, self.slots_number + 1):
            self.table.create_slot(self.slot_id)

        for player_id in players:
            self.table.create_player(player_id)
        pass

    def create_deck(self):
        card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_suits = ['♠', '♦', '♥', '♣']
        self.deck = []

        for suit in card_suits:
            for value in card_values:
                self.deck.append(value + suit)

        return self.deck


class Table:

    def __init__(self, slot_numbers: int):
        self.slot_numbers = slot_numbers
        self.slots = [Player_Slot(f"slot_{i}") for i in range(slot_numbers)]
        self.players = []
        self.player_slots = []

    def create_player(self, player_id: str):  # player takes a seat
        self.players.append(Player(player_id))

    def create_slot(self, slot_id: int):
        self.player_slots.append(Player_Slot(slot_id))


class Player_Slot:
    def __init__(self, slot_id: str):
        self.slot_id = slot_id


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.player_hand = []


the_list_of_players = ['soawesomesonic', 'filinfilin', 'Nightcrowler28', '1', '3', '5', '88', '99']
dealer = Dealer()
dealer.rule_game(the_list_of_players)
print(dealer.table.player_slots[7].slot_id)
