import random


class Dealer:
    """
    game logic class, created for rule the game

    """

    def __init__(self):  # initialization
        pass

    def rule_game(self):  # rule game
        pass


class Round:
    """
    class for game rounds.
    each new round:
        * create Table
        * create Table_Slots, bend Players to the Table_Slot by slot.id
        * create deck
        * # todo give cards from the deck to the Table_Slots

    players - list of players, inputted by user interface !blackjack
        example of list:
                        ['dealer', 'soawesomesonic', 'filinfilin', 'Nightcrowler28', '1', '3', '5', '88', '99']

    """

    def __init__(self, players: list):
        self.slots = []
        self.deck = []
        self.max_slots = 7  # numbers of possible players at the table, defines from rules of the game

        self.table = Table()

        for slot_id in range(0, len(players)):  # putting the Players to the Table_Slots
            if len(self.table.table_slots) < self.max_slots + 1: # limit the number of players
                self.table.create_slot(slot_id)
                self.table.create_player(players[slot_id])
        self.create_deck()

    def create_deck(self):
        card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_suits = ['♠', '♦', '♥', '♣']

        for suit in card_suits:
            for value in card_values:
                self.deck.append(value + suit)

        return self.deck


class Table:

    def __init__(self):
        self.players = []
        self.table_slots = []

    def create_player(self, player_id: str):  # player enters the table and want to play
        self.players.append(Player(player_id))

    def create_slot(self, slot_id: int):
        self.table_slots.append(Table_Slot(slot_id))

    def player_take_slot(self, player_id: str):
        pass


class Table_Slot:
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


the_list_of_players = ['dealer', 'soawesomesonic', 'filinfilin', 'Nightcrowler28', '1', '3', '5', '88', '99', 'dealer']

dealer = Dealer()
new_round = Round(the_list_of_players)
deck = new_round.create_deck()


for i in range(0, len(new_round.table.table_slots)):
    print(i, new_round.table.table_slots[i].slot_id)

for i in range(0, len(new_round.table.players)):
    print(i, new_round.table.players[i].player_id)

print(deck)