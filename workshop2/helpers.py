from workshop2 import setup


def select_a_sign():
    player_1_sign = input("Player one, please select a sign X or O: ")
    return player_1_sign

def select_position(counter):
    selected_position = input(f"{setup.player_names[counter % 2]}, select a position [1-9]: ")
    return selected_position

def turn_position_into_int(position):
    return int(position)

def print_info_about_game(name):
    print("This is the numeration of the board")
    print("|1|2|3|")
    print("|4|5|6|")
    print("|7|8|9|")
    print(f"{name} starts first")


def insert_player_names():
    player_1_name = input("Player one name: ")
    player_2_name = input("Player two name: ")
    return player_1_name, player_2_name


# def play_again():
#     new_game = input("Do you want to play again y/n: ")
#     while new_game not in ("y", "n"):
#         new_game = input("Do you want to play again y/n: ")
#
#     while new_game == "y":
#         setup()
#         play()
#         new_game = input("Do you want to play again y/n: ")
#     print("Bye! See you soon")

position_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}