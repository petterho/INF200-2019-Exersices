import random

def number_of_cards():
    number_of_card = []
    for number in range(1, 14):
        number_of_card.append(number)

    return number_of_card


def create_deck_of_cards():
    deck =[]
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    for suit in suits:
        deck.append((suit, number_of_cards()))

    return deck

def shuffle_deck():
    return random.shuffle(create_deck_of_cards())

def create_board():
    board = {}
    for position in range(1,14):
        board[position] = None

    return board

def play_single_round(board):
    pass



def check_winning_board():
    pass


print(create_deck_of_cards())

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print("{} of {}".format(self.value, self.suit))







