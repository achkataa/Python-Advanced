DEFAULT_ROWS_COUNT = 6
DEFAULT_COLUMN_COUNT = 7
DEFAULT_WIN_COUNT = 4


def get_player_choice(player):
    print(f"Player {player}, please choose a column")
    choice = int(input()) - 1
    return choice

def if_in_range(value, max_value):
    return 0 <= value < max_value


def is_win_condition(board, row_index, col_index, player, rows_count, cols_count):
    return if_in_range(row_index, rows_count) \
           and if_in_range(col_index, cols_count) \
           and board[row_index][col_index] == player




def has_win_condition_from_position(board, row_index, col_index, player, win_count=DEFAULT_WIN_COUNT):
    rows_count = len(board)
    cols_count = len(board[0])
    horizontal = [is_win_condition(board, row_index, col_index + d, player, rows_count, cols_count) for d in range(win_count)]
    vertical = [is_win_condition(board, row_index + d, col_index, player, rows_count, cols_count) for d in range(win_count)]
    right_diagonal = [is_win_condition(board, row_index + d, col_index + d, player, rows_count, cols_count) for d in range(win_count)]
    left_diagonal = [is_win_condition(board, row_index + d, col_index - d, player, rows_count, cols_count) for d in range(win_count)]

    return all(horizontal) or all(vertical) or all(right_diagonal) or all(left_diagonal)


def check_win_condition(board, player):
    rows_count = len(board)
    cols_count = len(board[0])
    for row_index in range(rows_count):
        for col_index in range(cols_count):
            if has_win_condition_from_position(board, row_index, col_index, player):
                return True
    return False

def get_lowest_free_row_index(board, col_index, player):
    rows_count = len(board)
    for row_index in range(rows_count-1, -1, -1):
        try:
            if board[row_index][col_index] == 0:
                return row_index
            continue
        except:
            print("Invalid Column")
            play(board, player)


def apply_player_choice(board, col_index, player):
    row_index = get_lowest_free_row_index(board, col_index, player)
    board[row_index][col_index] = player

def print_board(board):
    for row in board:
        print(row)

def print_winner(player):
    print(f"The winner is player {player}")


def play(board, player=1):
    while True:
        player_choice = get_player_choice(player)
        apply_player_choice(board, player_choice, player)
        print_board(board)
        if check_win_condition(board, player):
            print_winner(player)
            break
        player = 2 if player == 1 else 1

def create_board(rows = DEFAULT_ROWS_COUNT, cols = DEFAULT_COLUMN_COUNT):
    return [[0] * cols for _ in range(rows)]

board = create_board()

play(board)


