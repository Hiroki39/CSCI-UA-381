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


def set_up_turtles():
    global my_screen
    global my_turtle
    global screen_width
    global screen_height
    global my_screen
    global my_turtle
    global screen_up
    my_screen = turtle.Screen()
    my_turtle = turtle.Turtle()
    my_screen.colormode(255)
    screen_width, screen_height = my_screen.screensize()
    screen_up = True


def average(list_of_nums):
    total = 0
    for num in list_of_nums:
        total = total + num
    if len(list_of_nums) > 0:
        return(total / len(list_of_nums))


def fill_in_turn(player, center):
    my_turtle.pu()
    my_turtle.setposition(center[0], center[1])
    if player == 'X':
        my_turtle.setheading(45)
        my_turtle.fd(.1 * screen_width)
        my_turtle.left(180)
        my_turtle.pd()
        my_turtle.fd(.2 * screen_width)
        my_turtle.left(180)
        my_turtle.pu()
        my_turtle.fd(.1 * screen_width)
        my_turtle.left(90)
        my_turtle.fd(.1 * screen_width)
        my_turtle.left(180)
        my_turtle.pd()
        my_turtle.fd(.2 * screen_width)
    else:
        my_turtle.setheading(270)
        my_turtle.fd(.1 * screen_width)
        my_turtle.left(90)
        my_turtle.pd()
        my_turtle.circle(.1 * screen_width)


def go_turtle_tic_tac_toe_turn(player, row_centers, rows):
    print('Rows are numbered 1 to 3 from left to right.')
    print('Columns are numbered 1 to 3 from top to botton.')
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
            # fill_in_turn the main difference between the turtle version
            # and the text version of the program
            fill_in_turn(player, row_centers[row - 1][col - 1])
        else:
            print('Row', row, 'Column', col,
                  'is already occupied. Please choose again.')
            row = False
            col = False
        print('Game So Far')
        for row in rows:
            print(row)
        # The rest of the code checks if any player has won
        # check if same in a row
        for row_list in rows:
            if (row_list[0] == player) and (row_list[1] == player) and (row_list[2] == player):
                return(player)
        # check if same in a column
        for num in range(2):
            if (rows[0][num] == player) and (rows[1][num] == player) \
               and (rows[2][num] == player):
                return(player)
        # check for diagonals
        if rows[1][1] == player:
            if (rows[0][0] == player) and (rows[2][2] == player):
                return(player)
            elif (rows[2][0] == player) and (rows[0][2] == player):
                return(player)


def turtle_tic_tac_toe():
    global screen_up
    if not screen_up:
        set_up_turtles()
    else:
        my_screen.reset()
    my_turtle.pu()
    y_positions = []
    x_positions = []
    my_turtle.setposition(.5 * screen_width, -.125 * screen_width)
    # add_x_y_positions(x_positions,y_positions)
    my_turtle.pd()
    my_turtle.setheading(180)
    my_turtle.fd(screen_width)
    # add_x_y_positions(x_positions,y_positions)
    my_turtle.pu()
    my_turtle.right(90)
    my_turtle.fd(.25 * screen_width)
    # add_x_y_positions(x_positions,y_positions)
    my_turtle.pd()
    my_turtle.right(90)
    my_turtle.fd(screen_width)
    # add_x_y_positions(x_positions,y_positions)
    my_turtle.pu()
    my_turtle.setposition(.125 * screen_width, .5 * screen_width)
    # add_x_y_positions(x_positions,y_positions)
    my_turtle.right(90)
    my_turtle.pd()
    my_turtle.fd(screen_width)
    # add_x_y_positions(x_positions,y_positions)
    my_turtle.pu()
    my_turtle.right(90)
    my_turtle.fd(.25 * screen_width)
    # add_x_y_positions(x_positions,y_positions)
    my_turtle.right(90)
    my_turtle.pd()
    my_turtle.fd(screen_width)
    # add_x_y_positions(x_positions,y_positions)
    center_positions = []
    off_center_number = average([.5 * screen_width, .125 * screen_width])
    row_centers = []
    for row_multiple in [[[-1, 1], [0, 1], [1, 1]], [[-1, 0], [0, 0], [1, 0]], [[-1, -1], [0, -1], [1, -1]]]:
        new_row = []
        for multiple in row_multiple:
            # print(multiple)
            new_row.append([multiple[0] * off_center_number,
                            multiple[1] * off_center_number])
        row_centers.append(new_row)
    rows = []
    for num in range(3):
        row = ['_'] * 3
        rows.append(row)
    turns = 0
    player = 'X'
    # print(rows)
    # print(row_centers)
    win = False
    while (not win) and (turns < 9):
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        win = go_turtle_tic_tac_toe_turn(player, row_centers, rows)
        turns = turns + 1
    my_turtle.pu()
    my_turtle.setposition(-.75 * screen_width, .75 * screen_width)
    my_turtle.pencolor(250, 0, 0)
    my_turtle.pd()
    if win in ['X', 'O']:
        my_turtle.write(player + ' wins!!!!!!', font=('Arial', 30, 'bold'))
    else:
        my_turtle.write('It is a draw!!!!!', font=('Arial', 30, 'bold'))
    my_turtle.pu()
    my_turtle.pencolor('black')
