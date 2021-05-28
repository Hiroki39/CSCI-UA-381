import turtle
import random

screen_up = False


def get_remainders(rows, row, col):
    row_lst = []
    col_lst = []
    for i in range(3):
        if i == col:
            continue
        row_lst.append(rows[row][i])
    for i in range(3):
        if i == row:
            continue
        col_lst.append(rows[i][col])
    remainders = [row_lst, col_lst]
    if row == 0 and col == 0:
        remainders.append([rows[1][1], rows[2][2]])
    elif row == 0 and col == 2:
        remainders.append([rows[1][1], rows[2][0]])
    elif row == 2 and col == 0:
        remainders.append([rows[1][1], rows[0][2]])
    elif row == 2 and col == 2:
        remainders.append([rows[1][1], rows[0][0]])
    elif row == 1 and col == 1:
        remainders.append([rows[0][0], rows[2][2]])
        remainders.append([rows[0][2], rows[2][0]])
    return remainders


def go_tic_tac_toe_turn(player, rows, ai_turn):
    print('Rows are numbered 1 to 3 from top to botton.')
    print('Columns are numbered 1 to 3 from left to right.')
    row = False
    col = False
    done = False
    opponent = 'O' if player == 'X' else 'X'
    while not done:
        if not ai_turn:
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
        else:
            position_dict = {}
            for i in range(3):
                for j in range(3):
                    if rows[i][j] == '_':
                        # encode row and column by a single integer
                        position_dict[i * 3 + j] = get_remainders(rows, i, j)

            for key in position_dict:  # win
                if [player, player] in position_dict[key]:
                    rows[key // 3][key % 3] = player
                    done = True
                    break

            if not done:  # block
                for key in position_dict:
                    if [opponent, opponent] in position_dict[key]:
                        rows[key // 3][key % 3] = player
                        done = True
                        break

            if not done:  # fork
                for key in position_dict:
                    count = 0
                    for remainder in position_dict[key]:
                        if remainder in [[player, '_'], ['_', player]]:
                            count += 1
                    if count >= 2:
                        rows[key // 3][key % 3] = player
                        done = True
                        break

            if not done:  # block fork
                for key in position_dict:
                    count = 0
                    for remainder in position_dict[key]:
                        if remainder in [[opponent, '_'], ['_', opponent]]:
                            count += 1
                    if count >= 2:
                        force_block = False
                        for key2 in position_dict:
                            if [player, '_'] in position_dict[key] or ['_', player] in position_dict[key2]:
                                # forcing opponent block rather than fork
                                rows[key2 // 3][key2 % 3] = player
                                force_block = True
                                break
                        if not force_block:
                            # forcing opponent block rather than fork
                            rows[key // 3][key % 3] = player
                        done = True
                        break

            if not done:  # play center
                if 4 in position_dict:
                    rows[1][1] = player
                    done = True

            corners = [0, 2, 6, 8]
            random.shuffle(corners)

            if not done:  # play opposite corner
                for pos in corners:
                    if rows[pos // 3][pos % 3] == opponent and rows[2 - pos // 3][2 - pos % 3] == '_':
                        rows[2 - pos // 3][2 - pos % 3] = player
                        done = True
                        break

            if not done:  # play empty corner
                for pos in corners:
                    if pos in position_dict:
                        rows[pos // 3][pos % 3] = player
                        done = True
                        break

            if not done:  # play emptyside
                pos = random.choice(list(position_dict.keys()))
                rows[pos // 3][pos % 3] = player
                done = True

        print('Game So Far')
        for row in rows:
            print(row)
        # The rest of the code checks if any player has won
        # check if same in a row
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
    human_player = False
    while human_player not in ['O', 'X']:
        human_player = input(
            "Enter 'O' or 'X' to indicate which one you want to play: ")
        if human_player not in ['O', 'X']:
            print(human_player, "is an invalid input -- 'O' or 'X' only")
    turns = 0
    curr_player = 'X'
    win = False
    while (not win) and (turns < 9):
        if curr_player == 'X':
            curr_player = 'O'
        else:
            curr_player = 'X'
        win = go_tic_tac_toe_turn(
            curr_player, rows, curr_player != human_player)
        turns = turns + 1
    if win in ['X', 'O']:
        print(curr_player + ' wins!!!!!!')
    else:
        print('It is a draw!!!!!')
