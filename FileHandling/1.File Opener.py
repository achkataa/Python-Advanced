# try:
#     open("text.txt")
#     print("File found")
# except:
#     print("File not found")


try:
    with open("text.txt") as file:
        print("File found")
except FileNotFoundError:
    print("File not found")