import sys
def print_forsyth_edwards_notation(input: str) -> None:
    """
    Takes a FEN string and prints the board.
    """
    board = input.split()[0]
    board = board.split('/')
    for row in board:
        for cell in row:
            if cell.isdigit():
                print(' '*int(cell), end='')
            elif cell == 'K':
                print('♔', end='')
            elif cell == 'Q':
                print('♕', end='')
            elif cell == 'R':
                print('♖', end='')
            elif cell == 'B':
                print('♗', end='')
            elif cell == 'N':
                print('♘', end='')
            elif cell == 'P':
                print('♙', end='')
            elif cell == 'k':
                print('♚', end='')
            elif cell == 'q':
                print('♛', end='')
            elif cell == 'r':
                print('♜', end='')
            elif cell == 'b':
                print('♝', end='')
            elif cell == 'n':
                print('♞', end='')
            elif cell == 'p':
                print('♟', end='')
        print()
    print()

for a in sys.argv[1:]:
    print_forsyth_edwards_notation(a)