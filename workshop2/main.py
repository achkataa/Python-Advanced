from workshop2.setup import setup
from workshop2.play_engine import play

def play_again():
    new_game = input("Do you want to play again y/n: ")
    while new_game not in ("y", "n"):
        new_game = input("Do you want to play again y/n: ")

    while new_game == "y":
        setup()
        play()
        new_game = input("Do you want to play again y/n: ")
    print("Bye! See you soon")

if __name__ == "__main__":
    setup()
    play()
    play_again()

