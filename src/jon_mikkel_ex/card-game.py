from random import shuffle


def play_game():
    """ Play a single game of modified clock patience.
    Returns
    -------
    win: bool
        True if the game resulted in a win and False otherwise
    """
    cards = create_deck_of_cards()
    shuffle(cards)
    board = create_board()

    while not game_finished(cards, board):
        cards, board = play_single_round(cards, board)

    return is_winning_state(board)


def create_deck_of_cards():
    """ Returns a deck of cards represented by a list of 2-tuples.

    Each tuple represents one card, the first element is either
    ``'C'``, ``'D'``, ``'H'``, ``'S'``, representing clubs, diamonds, hearts and spades,
    The  second element represent the value of the card. 1 is ace, 11 is jack, 12, is queen, and 13 is king
    """
    suits = ['C', 'D', 'H', 'S']
    return [(suit, value) for suit in suits for value in range(1, 14)]


def create_board():
    """ Create an emptt board with 13 2-tuples containing ``None`` values
    """
    return [(None, None) for _ in range(13)]


def game_finished(cards, board):
    """ Returns True if the game is over, False otherwise,
    """
    return is_winning_state(board) or (len(cards) == 0)


def is_winning_state(board):
    for position in range(13):
        if board[position][1] != position + 1:
            return False

    return True


def play_single_round(cards, board):
    """ Play a single round of clock patience

    Returns
    -------
    cards: list
        Deck of cards after playing a round
    board: list
        Board state after playing a round
    """
    for position, board_state in enumerate(board):
        if board_state == position + 1:
            continue
        if len(cards) == 0:
            break
        board[position] = cards.pop()

    return cards, board



