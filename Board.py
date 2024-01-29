from Square import Square

BOARD_SIZE = 8

WPAWN = "P "
WKING = "K "
WQUEEN = "Q "
WBISHOP = "B "
WKNIGHT = "N "
WROOK = "R "

BPAWN = "p:"
BKING = "k:"
BQUEEN = "q:"
BBISHOP = "b:"
BKNIGHT = "n:"
BROOK = "r:"

RANK_LINE = "   ========================"
FILES = "    A  B  C  D  E  F  G  H "

class Board:


    def __init__(self, players):
        self.check = False
        self.checkmate = False
        self.stalemate = False
        self.draw = False
        self.player_turn = False #In other words player 0
        self.players = players

    def build_board(self):

        self.board = [[Square("WHITE" if (rank + file) % 2 == 0 else "BLACK") for file in range(0,BOARD_SIZE)] for rank in range(0,BOARD_SIZE)]
        
        #PAWNS
        for file in range(0,BOARD_SIZE):
            self.board[1][file].set_man(WPAWN)
            self.board[1][file].set_occupied(True)

        for file in range(0,BOARD_SIZE):
            self.board[6][file].set_man(BPAWN)
            self.board[6][file].set_occupied(True)

        #KING+QUEEN
        self.board[0][4].set_man(WKING)
        self.board[0][4].set_occupied(True)
        self.board[7][4].set_man(BKING)
        self.board[7][4].set_occupied(True)

        self.board[0][3].set_man(WQUEEN)
        self.board[0][3].set_occupied(True)
        self.board[7][3].set_man(BQUEEN)
        self.board[7][3].set_occupied(True)

        #BISHOP
        self.board[0][2].set_man(WBISHOP)
        self.board[0][2].set_occupied(True)
        self.board[0][5].set_man(WBISHOP)
        self.board[0][5].set_occupied(True)
        self.board[7][2].set_man(BBISHOP)
        self.board[7][2].set_occupied(True)
        self.board[7][5].set_man(BBISHOP)
        self.board[7][5].set_occupied(True)

        #KNIGHT
        self.board[0][1].set_man(WKNIGHT)
        self.board[0][1].set_occupied(True)
        self.board[0][6].set_man(WKNIGHT)
        self.board[0][6].set_occupied(True)
        self.board[7][1].set_man(BKNIGHT)
        self.board[7][1].set_occupied(True)
        self.board[7][6].set_man(BKNIGHT)
        self.board[7][6].set_occupied(True)

        #ROOK
        self.board[0][0].set_man(WROOK)
        self.board[0][0].set_occupied(True)
        self.board[0][7].set_man(WROOK)
        self.board[0][7].set_occupied(True)
        self.board[7][0].set_man(BROOK)
        self.board[7][0].set_occupied(True)
        self.board[7][7].set_man(BROOK)
        self.board[7][7].set_occupied(True)

    def print_board(self):
        print("\n\n" + RANK_LINE)
        for rank in range(BOARD_SIZE,0,-1):
            print("{} |".format(rank),end="")
            for file in range(BOARD_SIZE,0,-1):
                print("{}|".format(self.board[rank-1][file-1].get_man()),end="")
            
            print("\n" + RANK_LINE)
        
        print(FILES)

        