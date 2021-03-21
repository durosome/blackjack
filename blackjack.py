import random


class Dealer:
    """
    game logic class, created for rule the game

    """

    def __init__(self):  # initialization
        pass

    def count_hand(self, hand):
        hand_sum = 0

        for i in range(0, len(hand)):
            hand[i] = hand[i][:1]  # clean from suits
            try:
                int(hand[i])
                hand_sum = hand_sum + int(hand[i])
            except:
                hand_sum = hand_sum + 0
                if hand[i] == 'K':
                    hand_sum = hand_sum + 10
                if hand[i] == 'Q':
                    hand_sum = hand_sum + 10
                if hand[i] == 'J':
                    hand_sum = hand_sum + 10
                if hand[i] == 'A':
                    hand_sum = hand_sum + 0

        for i in range(0, len(hand)):
            if hand[i] == 'A':
                if hand_sum < 11:
                    hand_sum = hand_sum + 11
                else:
                    hand_sum = hand_sum + 1


        return (hand_sum)

    def rule_game(self):  # rule game
        pass




class Round:
    """
    class for game rounds.
    each new round:
        * create Table
        * create Table_Slots, bend Players to the Table_Slot by slot.id
        * create deck
        * give cards from the deck to the Table_Slots

    players - list of players, inputted by user interface !blackjack
        example of list:
                        ['dealer', 'soawesomesonic', 'filinfilin', 'Nightcrowler28', '1', '3', '5', '88', '99']

    """

    def __init__(self, players: list):
        self.slots = []
        self.deck = []
        self.max_slots = 7  # numbers of possible players at the table, defines from rules of the game

        self.table = Table()
        self.create_deck()

        for slot_id in range(0, len(players)):  # putting the Players to the Table_Slots
            if len(self.table.table_slots) < self.max_slots + 1:   # limit the number of players
                self.table.create_player(players[slot_id])         # create player
                self.table.create_slot(slot_id, players[slot_id])  # create slot
                self.put_card_in_hand(self.table.table_slots[slot_id].hand)
                self.put_card_in_hand(self.table.table_slots[slot_id].hand)

    def create_deck(self):
        card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_suits = ['♠', '♦', '♥', '♣']

        for suit in card_suits:
            for value in card_values:
                self.deck.append(value + suit)

        return self.deck

    def give_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        return card

    def put_card_in_hand(self, hand):
        card = self.give_card()
        hand.append(card)
        return card


class Table:

    def __init__(self):
        self.players = []
        self.table_slots = []

    def create_player(self, player_id: str):  # player enters the table and want to play
        self.players.append(Player(player_id))

    def create_slot(self, slot_id: int, player_id):
        self.table_slots.append(Table_Slot(slot_id, player_id))


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
            - Dealer.Table.Table_Slot[11].slot_id
                --it will return us a player_id, looks like: '11'

            * player_id
                    is player in 7th slot on the table
            - Dealer.Table.Table_Slot[7].player_id
                -it will return us a player_id, looks like: 'soawesomesonic'

            * hand
                    hand of player in 3rd slot on the table
            - Round.Table.Table_Slot[3].hand
                -it will return us a hand, looks like: ['4♣', 'K♦']

    """

    def __init__(self, slot_id: int, player_id: str):
        self.slot_id = slot_id
        self.player_id = player_id
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

for i in range(0, len(new_round.table.table_slots)):
    print(new_round.table.table_slots[i].player_id, 's hand: ', new_round.table.table_slots[i].hand, 'Value: ', dealer.count_hand(new_round.table.table_slots[i].hand))