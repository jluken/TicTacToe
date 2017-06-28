def display(board, user_sym):
    if user_sym == 'X':
        ai_sym = 'O'
    else:
        ai_sym = 'X'
    sym_board = [['','',''],['','',''],['','','']]
    for column in range(3):
        for row in range(3):
            if board[column][row] == 0:
                sym_board[column][row] = ' '
            elif board[column][row] == 1:
                sym_board[column][row] = user_sym
            else:
                sym_board[column][row] = ai_sym
    print_board = '\n'
    print_board += '      |     |     \n'
    print_board += '3  '+sym_board[0][2]+'  |  '+sym_board[1][2]+'  |  '+sym_board[2][2]+'  \n'
    print_board += ' _____|_____|_____\n'
    print_board += '      |     |     \n'
    print_board += '2  '+sym_board[0][1]+'  |  '+sym_board[1][1]+'  |  '+sym_board[2][1]+'  \n'
    print_board += ' _____|_____|_____\n'
    print_board += '      |     |     \n'
    print_board += '1  '+sym_board[0][0]+'  |  '+sym_board[1][0]+'  |  '+sym_board[2][0]+'  \n'
    print_board += '      |     |     \n'
    print_board += '   A     B     C   '
    return print_board

def player_turn(board, user_sym):
    while True:
        input = raw_input("Where would you like to move? ")
        A = 'A' in input or 'a' in input
        B = 'B' in input or 'b' in input
        C = 'C' in input or 'c' in input
        _1 = '1' in input
        _2 = '2' in input
        _3 = '3' in input
        if (A and B) or (A and C) or (B and C) or (_1 and _2) or (_1 and _3) or (_2 and _3):
            print "I'm sorry. That was not a valid board space. Please only include one of each column and row."
            continue
        if A:
            x_val = 0
        elif B:
            x_val = 1
        elif C:
            x_val = 2
        else:
            print "I'm sorry. That was not a valid board space. Please include the column letter. "
            continue
        if _1:
            y_val = 0
        elif _2:
            y_val = 1
        elif _3:
            y_val = 2
        else:
            print "I'm sorry. That was not a valid board space. Please include the row number. "
            continue
        if board[x_val][y_val] != 0:
            print "That space is already taken, please pick another. "
            continue
        break

    board[x_val][y_val] = 1

    print display(board, user_sym)

    result = check_win(board)
    if result == None:
        result = ai_turn(board, user_sym)

    return result

def ai_turn(board, user_sym):
    print "Now it's my turn. "
    board_options = minimax(board, -1)

    move_row = 0
    move_column = 0
    for column in range(3):
        for row in range(3):
            if board_options[move_column][move_row] is None:
                move_column = column
                move_row = row
            elif board_options[column][row] is not None and board_options[column][row] < board_options[move_column][move_row]:
                move_column = column
                move_row = row

    board[move_column][move_row] = -1

    print display(board, user_sym)

    result = check_win(board)
    if result == None:
        result = player_turn(board, user_sym)

    return result

def minimax(board, player):
    mm_board = [[None,None,None],[None,None,None],[None,None,None]]
    for column in range(3):
        for row in range(3):
            if board[column][row] == 0:
                board_copy = [[0,0,0],[0,0,0],[0,0,0]]
                for board_column in range(3):
                    for board_row in range(3):
                        board_copy[board_column][board_row] = board[board_column][board_row]
                board_copy[column][row] = player
                result = check_win(board_copy)
                if result != None:
                    mm_board[column][row] = result
                else:
                    result = minimax(board_copy, -player)
                    best_outcome = player
                    lose = False
                    for result_column in range(3):
                        for result_row in range(3):
                            if result[result_column][result_row] == -player:
                                best_outcome = -player
                                lose = True
                            elif result[result_column][result_row] == 0 and lose == False:
                                best_outcome = 0
                    mm_board[column][row] = best_outcome
                    if best_outcome == player:
                        return mm_board

    return mm_board

def check_win(board):
    players = [-1,1]
    for player in players:
        for line in range(3):
            if ((board[line][0] == player and board[line][1] == player and board[line][2] == player) or
                (board[0][line] == player and board[1][line] == player and board[2][line] == player)):
                return player
        if ((board[0][0] == player and board[1][1] == player and board[2][2] == player) or
            (board[0][2] == player and board[1][1] == player and board[2][0] == player)):
            return player
    over = True
    for column in board:
        for row in column:
            if row == 0:
                over = False
    if over:
        return 0
    return None



def intro():
    input = raw_input("Welcome to Tic Tac Toe. Would you like to bs Xs or Os? ")
    while True:
        if input in ['x','X','xs','Xs', 'x\'s', 'X\'s']:
            user_sym = 'X'
            break
        elif input in ['o','O','os','Os', 'o\'s', 'O\'s']:
            user_sym = 'O'
            break
        else:
            input = raw_input("That is not a valid input. Would you like to bs Xs or Os? ")

    board = [[0,0,0],[0,0,0],[0,0,0]]
    board_display = display(board, user_sym)
    print board_display

    if user_sym == 'X':
        ending = player_turn(board, user_sym)
    else:
        ending = ai_turn(board, user_sym)
    end(ending)

def end(ending):
    if ending == 1:
        finale = "Congratulations! You've won! Press \'r\' to restart, or press \'q\' to quit. "
    elif ending == -1:
        finale = "Sorry, you lose. Would you like to try again? Press \'r\' to restart, or press \'q\' to quit. "
    else:
        finale = "It's a draw. Would you like to try again? Press \'r\' to restart, or press \'q\' to quit. "
    input = raw_input(finale)
    if input in ['r', 'R']:
        intro()
    elif input in ['q', 'Q']:
        quit = True
    else:
        while True:
            input = raw_input("Sorry, that's an invalid entry. Press \'r\' to restart, or press \'q\' to quit. ")
            if input in ['r', 'R']:
                intro()
            elif input in ['q', 'Q']:
                quit = True

intro()
