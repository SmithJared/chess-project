import Square

class Board:

    BOARD_SIZE = 8

    def __init__(self, players):
        self.check = False
        self.checkmate = False
        self.stalemate = False
        self.draw = False
        self.player_turn = False #In other words player 0
        self.players = players

    def build_board():
        board = []
        