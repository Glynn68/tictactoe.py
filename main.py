import numpy as np
import os
import time
board = np.array([[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']])
guide_board = np.array([['0','1','2'], ['3','4','5'], ['6','7','8']])
input_err = 1
computer_move_completed = type(bool)
move = 0
row = 0
col = 0
row_posn_diag = (0, 1, 2)
col_posn_diag_STL = (0, 1, 2)
col_posn_diag_STR = (2, 1, 0)
a = 'XX '
b = 'X X'
c = ' XX'
e = 'OO '
f = 'O O'
g = ' OO'
def get_player_move(input_err, board):
    """ Get input from player, check if valid and convert to row and column"""
    row = 0
    col = 0
    print(guide_board)
    player_move = int(input('Enter your move (0 to 8) '))
    print()
    print('You entered', player_move)
    print()
#
    if -1 < player_move < 3:
        row = 0
        col = player_move 
        input_err = 0
#           
    elif 2 < player_move < 6:
        row = 1
        col = player_move -3
        input_err = 0
#    
    elif 5 < player_move < 9:
        row = 2
        col = player_move - 6
        input_err = 0
# Check if value in range 0 to 8
    else:
        os.system("clear")
        print('Sorry your entry is not in range 0 to 8')
        print()
        print(board)
        print()
        input_err = 1
# Check if space already occupied    
    if board[row,col] != ' ':
        os.system("clear")
        print('Sorry that space is already occupied')
        print()
        print(board)
        print()
        input_err = 1
    return row,col,input_err   
#
#
def computer_win(row, col, board):
    board[row,col] = 'X'
    print('Computer wins')
    print()
    print(board)
    print()
    print('Goodbye!')
    quit()
#
#
# 
def two_of_a_kind_in_a_row(a, b, c, board, computer_move_completed, row, col):     
    for row in range(3):
        d = ''.join(board[row,0:3])
        if d == a or d == b or d == c:
            for col in range(3):
                if board[row,col] == ' ':
                    board[row,col] = 'X'
                    computer_move_completed = True
    return row, col, board, computer_move_completed
#
def two_of_a_kind_in_a_col(a, b, c, board, computer_move_completed, row, col):     
    for col in range (3):
        d = board[0,col] + board[1,col] + board[2,col]
        if d == a or d == b or d == c:
            for row in range(3):
                if board[row,col] == ' ':
                    board[row,col] = 'X'
                    computer_move_completed = True
    return row, col, board, computer_move_completed   
#
def two_of_a_kind_on_a_diagonal(a, b, c, board, computer_move_completed, row_posn_diag, col_posn_diag):
    row = 0
    col = 0
    d = board[0,col_posn_diag[0]] + board[1,col_posn_diag[1]] + board[2,col_posn_diag[2]]
    if d == a or d == b or d == c:
        for row, col in zip(row_posn_diag, col_posn_diag):
            if board[row,col] == ' ':
                board[row,col] = 'X'
                computer_move_completed = True
    return row, col, board, computer_move_completed
#
# Main
while move < 10:
    os.system("clear")
    print('Move = ', move)
    print()
    print(board)
    print()
    while input_err == 1:
        row, col, input_err = get_player_move(input_err, board)
    board[row,col] = 'O'
    move += 1
    print('Move = ', move)
    print()
    print(board)
    print()
    input_err = 1
    #If it's a draw after 9 moves, end the game
    if move == 9:
        print('Well played, it\'s a draw!')
        print('Goodbye!')
        quit()
    #
    #
    #   Start of Computer Move
    #
    print('I am thinking......')
    time.sleep(3) #wait a few seconds
    computer_move_completed = False
    #
    #
    # For first computer move, best to place X in centre of board if player hasn't placed there already
    #   If move = 1 , check if X can be placed in centre
    if move == 1 and board[1,1] == ' ':
        board[1,1] = 'X'
        computer_move_completed = True
    #
    # 
    # For second computer move, check for O's in diagonally opposite corners, if so, place X in side square
    if move == 3:
        if (board[0,0] == 'O' and board[2,2] == 'O') or (board[0,2] == 'O' and board[2,0] == 'O'):
            board[0,1] = 'X'
            computer_move_completed = True
    #
    # Check if 3rd of 3 X's can be placed in a row
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_in_a_row(a, b, c, board, computer_move_completed, row, col)
        if computer_move_completed == True:
            computer_win(row, col, board)
    #
    # Check if 3rd of 3 X's can be placed in a column
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_in_a_col(a, b, c, board, computer_move_completed, row, col)
        if computer_move_completed == True:
            computer_win(row, col, board)
    #
    # Check if 3rd of 3 X's can be placed on diagonal Starting Top Left (STL)
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_on_a_diagonal(a, b, c, board, computer_move_completed, row_posn_diag, col_posn_diag_STL)
        if computer_move_completed == True:
            computer_win(row, col, board)
    #
    # Check if 3rd of 3 X's can be placed on diagonal Starting Top Right (STR)
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_on_a_diagonal(a, b, c, board, computer_move_completed, row_posn_diag, col_posn_diag_STR)
        if computer_move_completed == True:
            computer_win(row, col, board)
    #     
    # Check if there are 2 O's in any row without X
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_in_a_row(e, f, g, board, computer_move_completed, row, col)
    #
    # Check if there are 2 O's in any column without X
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_in_a_col(e, f, g, board, computer_move_completed, row, col)
    #
    # Check if there are 2 O's in diagonal without X starting top left
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_on_a_diagonal(e, f, g, board, computer_move_completed, row_posn_diag, col_posn_diag_STL)
    #
    # Check if there are 2 O's in diagonal without X starting top right
    if computer_move_completed == False:
        row, col, board, computer_move_completed = two_of_a_kind_on_a_diagonal(e, f, g, board, computer_move_completed, row_posn_diag, col_posn_diag_STR)
    #
    # Check if X can be placed in a corner, if not place in free side square
    cs_posn = (0, 0, 0, 2, 2, 0, 2, 2, 0, 1, 1, 0, 1, 2, 2, 1)# These are (row, col) positions of corner and side squares
    x = 0
    while computer_move_completed == False and x < 8:
        if board[cs_posn[x], cs_posn[x+1]] == ' ':
            board[cs_posn[x], cs_posn[x+1]] = 'X'
            computer_move_completed = True
        x += 2
#
#Computer move complete, increment move
    move += 1
