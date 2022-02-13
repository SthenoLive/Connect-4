"""
This will make a text based playable game of connect 4. Player 1 will 
be represented by X's and player 2 by O's.
"""

"""
This will make a coordinate grid of all of the spaces. A blank space 
will be a ' ' string, and the X's and O's will be 'X' and 'O' 
respectively. When calling a cell, the first number will call which row
and the second number will call which column. When counting, [0][0] will be
the top left and [6][6] will be the bottom right
"""

xy = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' '],
      [' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# ----------------------------------------------------------------------------------------------------------------------

# this will create the game board
board_close = '+---+---+---+---+---+---+---+'


def draw_board():
    print('  1   2   3   4   5   6   7  ')
    print(board_close)
    for i in range(7):
        print(f'| {xy[i][0]} | {xy[i][1]} | {xy[i][2]} | {xy[i][3]} | {xy[i][4]} | {xy[i][5]} | {xy[i][6]} |')
        print(board_close)


# ----------------------------------------------------------------------------------------------------------------------

# this will check if either player has won


def check_win(letter):
    for k in range(7):
        for i in range(4):
            if xy[i][k] == letter\
                    and xy[i + 1][k] == letter\
                    and xy[i + 2][k] == letter\
                    and xy[i + 3][k] == letter:
                return True
        for i in range(4):
            if xy[k][i] == letter\
                    and xy[k][i + 1] == letter\
                    and xy[k][i + 2] == letter\
                    and xy[k][i + 3] == letter:
                return True
    for k in range(4):
        for i in range(4):
            if xy[i][k] == letter\
                    and xy[i + 1][k + 1] == letter\
                    and xy[i + 2][k + 2] == letter\
                    and xy[i + 3][k + 3] == letter:
                return True
        for i in range(3, 6):
            if xy[k][i] == letter\
                    and xy[k + 1][i - 1] == letter\
                    and xy[k + 2][i - 2] == letter\
                    and xy[k + 3][i - 3] == letter:
                return True
    return False


# ----------------------------------------------------------------------------------------------------------------------

# this will allow a player to place a piece in any column
count = [0, 0, 0, 0, 0, 0, 0]  # the count will start at 0 and go down 1 for every time a piece is placed in its column
col = 0


def turn(piece):
    global col
    valid = False
    while not valid:
        col = int(input('Pick a column 1-7: '))
        if col >= 8:
            print('Invalid number, pick again')
        elif col <= 0:
            print('Invalid number, pick again')
        elif count[col - 1] == -7:
            print('Column is full, pick again')
        else:
            valid = True
    count[col - 1] -= 1
    xy[count[col - 1]][col - 1] = piece
    draw_board()
    if check_win(piece):
        return True


# ----------------------------------------------------------------------------------------------------------------------
win = False
# this will run the game
while not win:
    if not check_win('O'):
        if turn('X'):
            win = True
    if not check_win('X'):
        if turn('O'):
            win = True

# this will display text upon the game's completion
if check_win('X'):
    print('Player 1 wins!!!')
if check_win('O'):
    print('Player 2 wins!!!')
