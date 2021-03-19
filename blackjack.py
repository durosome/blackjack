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
        self.slots_number = 7  # numbers of possible players at the table, defines from rules of the game #TODO maybe we should create class Rules
        self.table = Table(self.slots_number)
        self.slots = []

        for self.slot_id in range(0, self.slots_number + 1): # +1, because we should reserve slot[0] for dealer
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
        self.players = []
        self.player_slots = []

    def create_player(self, player_id: str):  # player enters the table and want to play
        self.players.append(Player(player_id))

    def create_slot(self, slot_id: int):
        self.player_slots.append(Player_Slot(slot_id))

    def player_take_slot(self, player_id: str):
        pass



class Player_Slot:
    """
    1. we have a table
        --  [       ]
    2. this class adds a slots on it
        --  [ () () ]
    3. in each slot we store slot_id, hand, player_id
        example:
            column = objects
            row = attributes of objects

        --  [         (0)                  (1)           ]
            [    (['4♣', 'K♦'])      (['10♣', 'A♦'])    ]
            [       (dealer)        (soawesomesonic)    ]

    Dealer.Table.Player_Slot[0] is always reserved for DEALER

    example usage:
        we can get
            * slot_id
                    is basically positional number of slot #TODO maybe we can delete this attribute
            - Dealer.Table.Player_Slot[11].slot_id
                --it will return us a player_id, looks like: '11'

            * player_id
                    is player in 7th slot on the table
            - Dealer.Table.Player_Slot[7].player_id
                -it will return us a player_id, looks like: 'soawesomesonic'

            * hand
                    hand of player in 3rd slot on the table
            - Dealer.Table.Player_Slot[3].player_hand
                -it will return us a hand, looks like: ['4♣', 'K♦']

    """
    def __init__(self, slot_id: int):
        self.slot_id = slot_id
        self.player_id = ''
        self.hand = []


class Player:
    """
    now it's absolutely useless class, but in future we will add some attributes, like twitch_points
    example usage:
        we can get
            * player_id
                    just id of player
            - Dealer.Table.Player[0].player_id
                -it will return a player_id, looks like: 'dealer' #always return dealer from 0th slot, cause it reserves for DEALER

            - Dealer.Table.Player[1].player_id
                -it will return a player_id, looks like: 'soawesomesonic'


    """

    def __init__(self, player_id):
        self.player_id = player_id


the_list_of_players = ['dealer', 'soawesomesonic', 'filinfilin', 'Nightcrowler28', '1', '3', '5', '88', '99']
# the_list_of_players[0] should always be dealer

dealer = Dealer()
dealer.rule_game(the_list_of_players)

for i in range(0, len(dealer.table.player_slots)):
    print(i, dealer.table.player_slots[i].slot_id)

for i in range(0, len(dealer.table.players)):
    print(i, dealer.table.players[i].player_id)