import turtle

screen_up = False


def go_tic_tac_toe_turn(player, rows):
    print('Rows are numbered 1 to 3 from top to botton.')
    print('Columns are numbered 1 to 3 from left to right.')
    row = False
    col = False
    done = False
    while not done:
        while type(row) != int:
            answer = input('Indicate which row. ')
            if answer in '123':
                row = int(answer)
            else:
                print(answer, 'is an invalid row -- 1, 2 or 3 only')
        while type(col) != int:
            answer = input('Indicate which column. ')
            if answer in '123':
                col = int(answer)
            else:
                print(answer, 'is an invalid row -- 1, 2 or 3 only')
        row_list = rows[row - 1]
        if row_list[col - 1] == '_':
            row_list[col - 1] = player
            done = True
        else:
            print('Row', row, 'Column', col,
                  'is already occupied. Please choose again.')
            row = False
            col = False
        # check if same in a row
        print('Game So Far')
        for row in rows:
            print(row)
        # The rest of the code checks if any player has won
        for row_list in rows:
            if (row_list[0] == player) and (row_list[1] == player) and (row_list[2] == player):
                return(player)
        # check if same in a column
        for num in range(3):
            if (rows[0][num] == player) and (rows[1][num] == player) \
               and (rows[2][num] == player):
                return(player)
        # check for diagonals
        if rows[1][1] == player:
            if (rows[0][0] == player) and (rows[2][2] == player):
                return(player)
            elif (rows[2][0] == player) and (rows[0][2] == player):
                return(player)


def tic_tac_toe():
    rows = []
    for num in range(3):
        row = ['_', '_', '_']
        rows.append(row)
    turns = 0
    player = 'X'
    win = False
    while (not win) and (turns < 9):
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        win = go_tic_tac_toe_turn(player, rows)
        turns = turns + 1
    if win in ['X', 'O']:
        print(player + ' wins!!!!!!')
    else:
        print('It is a draw!!!!!')
