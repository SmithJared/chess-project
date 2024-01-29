from Board import Board

def main():

    board = Board(2)#Hardcoded two for testing. 
    board.build_board()
    board.print_board()

    # while(board.is_winner()):


if __name__ == "__main__":
    main()