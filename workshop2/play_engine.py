from workshop2 import setup
from workshop2.helpers import position_mapper, select_position, turn_position_into_int

def is_position_valid(pos):
    if pos in range(0, 10):
        return True
    return False

def position_available(board, pos):
    row, col = position_mapper[pos]
    if board[row][col] == " ":
        return True
    return False

def draw_board(board):
    for row in board:
        print(row)


def play_turn(board, sign, pos, counter):
    if position_available(board, pos):
        row, col = position_mapper[pos]
        board[row][col] = sign
        draw_board(board)
    else:
        selected_position = select_position(counter)
        selected_position = turn_position_into_int(selected_position)
        play_turn(board, sign, selected_position, counter)


def is_row_winner():
    for row_number in range(len(setup.board)):
        if setup.board[row_number].count("X") == 3 or setup.board[row_number].count("O") == 3:
            return True
    return False

def is_col_winner():
    for col_number in range(len(setup.board)):
        if setup.board[0][col_number] == setup.board[1][col_number] == setup.board[2][col_number] != " ":
            return True
    return False



def is_diagonal_winner():
    left_diagonal = setup.board[0][0] == setup.board[1][1] == setup.board[2][2] != " "
    right_diagonal = setup.board[0][2] == setup.board[1][1] == setup.board[2][0] != " "
    if left_diagonal or right_diagonal:
        return True
    return False


def has_won():
    if is_row_winner() or is_col_winner() or is_diagonal_winner():
        return True
    return False


def has_moves(counter):
    if counter > 9:
        return True
    return False


def play():
    counter = 1
    while not has_won():
        selected_position = select_position(counter)
        while not selected_position.isdigit():
            selected_position = select_position(counter)
        selected_position = turn_position_into_int(selected_position)
        while not is_position_valid(selected_position):
            selected_position = select_position(counter)
            selected_position = turn_position_into_int(selected_position)
        play_turn(setup.board, setup.player_signs[counter % 2], selected_position, counter)
        counter += 1
        if has_moves(counter):
            print("Nobody wins")
            return
    print(f"{setup.player_names[(counter - 1) % 2]} wins")



