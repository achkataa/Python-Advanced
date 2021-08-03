from workshop2.helpers import select_a_sign, print_info_about_game, insert_player_names

def setup():
    global player_1_name, player_2_name
    global board
    board = [[" ", " ", " "] for _ in range(3)]
    player_1_name, player_2_name = insert_player_names()
    player_1_sign = select_a_sign()
    while player_1_sign.lower() not in ("x", "o"):
        player_1_sign = select_a_sign()
    player_1_sign = player_1_sign.upper()
    player_2_sign = "O" if player_1_sign == "X" else "X"
    global player_signs, player_names

    player_signs = {1: player_1_sign, 0: player_2_sign}
    player_names = {1: player_1_name, 0: player_2_name}

    print_info_about_game(player_1_name)

